"""Build the example film soundtrack from audio/cues.json.

Run from <project>\\video with the Earshot venv (numpy, scipy, soundfile, pyloudnorm):

    ..\\tools\\earshot\\.venv\\Scripts\\python.exe -I audio\\mix.py            # writes assets/audio/refer-earn-mix.wav
    ..\\tools\\earshot\\.venv\\Scripts\\python.exe -I audio\\mix.py --stems    # also music-only / sfx-only stems for QA

Everything is deterministic and reproducible:
  * FFmpeg decodes every source to 48 kHz stereo float (set FFMPEG=... if ffmpeg is not on PATH).
  * Each cue is placed so its sync point (the loudest instant by default) lands exactly on the cue
    time `t` in film seconds. A whoosh therefore peaks on the cut, an impact hits on the frame.
  * Levels are relative: every cue is gain-matched so its loudest 100 ms (K-weighted) sits `rel` dB
    against the music's beat level (90th percentile of the music's 100 ms loudness, film 8-40 s).
  * The master is normalised to -14 LUFS integrated (BS.1770, pyloudnorm) with a 4x-oversampled
    look-ahead limiter holding true peak at or below -1 dBTP.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from fractions import Fraction

import numpy as np
import pyloudnorm as pyln
import soundfile as sf
from scipy.ndimage import minimum_filter1d, uniform_filter1d
from scipy.signal import butter, lfilter, resample_poly, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.dirname(HERE)
SR = 48000

KIND_REL = {  # default level of each kind of cue against the music's beat level (dB)
    "impact": -2.0,
    "hit": -6.0,
    "whoosh": -8.0,
    "riser": -8.0,
    "ui": -13.0,
    "tick": -15.0,
    "type": -17.0,
}


def find_ffmpeg():
    for cand in (os.environ.get("FFMPEG"), shutil.which("ffmpeg"),
                 r"ffmpeg.exe"):
        if cand and os.path.exists(cand):
            return cand
    sys.exit("ffmpeg not found: put it on PATH or set FFMPEG to its full path")


FF = find_ffmpeg()


def decode(path, ss=None, dur=None):
    cmd = [FF, "-v", "error"]
    if ss is not None:
        cmd += ["-ss", f"{ss:.6f}"]
    if dur is not None:
        cmd += ["-t", f"{dur:.6f}"]
    cmd += ["-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype="<f4").reshape(-1, 2).astype(np.float64)


# ---------------------------------------------------------------- measurement
KB1, KA1 = [1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585]
KB2, KA2 = [1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621]


def short_loudness(x, win=0.1, hop=0.01):
    """K-weighted loudness of sliding `win` windows (dB, BS.1770 scale) and their start times."""
    y = lfilter(KB2, KA2, lfilter(KB1, KA1, x, axis=0), axis=0)
    p = np.sum(y ** 2, axis=1)
    n = max(1, int(win * SR))
    c = np.concatenate([[0.0], np.cumsum(p)])
    starts = np.arange(0, max(1, len(p) - n + 1), max(1, int(hop * SR)))
    ms = (c[np.minimum(starts + n, len(p))] - c[starts]) / n
    return -0.691 + 10 * np.log10(ms + 1e-12), starts / SR


def level(x):
    return float(np.max(short_loudness(x)[0]))


def env_db(x, win=0.01):
    m = np.mean(x ** 2, axis=1)
    return 10 * np.log10(uniform_filter1d(m, max(1, int(win * SR))) + 1e-12)


def sync_point(x, how):
    if isinstance(how, (int, float)):
        return float(how)
    e = env_db(x)
    pk = int(np.argmax(e))
    if how == "peak":
        return pk / SR
    if how == "onset":  # first instant within 24 dB of the peak
        return int(np.nonzero(e[: pk + 1] > e[pk] - 24)[0][0]) / SR
    if how == "end":
        return len(x) / SR
    raise ValueError(f"unknown sync {how!r}")


def true_peak_db(x):
    up = resample_poly(x, 4, 1, axis=0)
    return 20 * np.log10(np.max(np.abs(up)) + 1e-12)


# ---------------------------------------------------------------- processing
def fade(x, fin, fout):
    n = len(x)
    if fin > 0:
        k = min(n, int(fin * SR))
        x[:k] *= np.linspace(0, 1, k, endpoint=False)[:, None] ** 2
    if fout > 0:
        k = min(n, int(fout * SR))
        x[n - k:] *= np.linspace(1, 0, k)[:, None] ** 2
    return x


def filt(x, hp=None, lp=None):
    if hp:
        x = sosfilt(butter(2, hp, "hp", fs=SR, output="sos"), x, axis=0)
    if lp:
        x = sosfilt(butter(2, lp, "lp", fs=SR, output="sos"), x, axis=0)
    return x


def pan(x, p):
    if not p:
        return x
    a = (p + 1) * np.pi / 4
    return x * np.array([np.cos(a), np.sin(a)]) * np.sqrt(2)


def automation(points, n, default=0.0):
    """Piecewise-linear dB curve from [[t, db], ...] sampled at SR, held flat outside the points."""
    if not points:
        return np.full(n, default)
    pts = sorted(points)
    t = np.arange(n) / SR
    return np.interp(t, [p[0] for p in pts], [p[1] for p in pts])


def limiter(x, ceiling_db, lookahead=0.0015, release=0.08):
    """Look-ahead peak limiter on the 4x-oversampled signal. Returns (y, max gain reduction dB)."""
    up = resample_poly(x, 4, 1, axis=0)
    pk = np.max(np.abs(up), axis=1).reshape(-1, 4).max(axis=1)[: len(x)]
    if len(pk) < len(x):
        pk = np.pad(pk, (0, len(x) - len(pk)))
    thr = 10 ** (ceiling_db / 20)
    g = np.minimum(1.0, thr / np.maximum(pk, 1e-12))
    if g.min() >= 1.0:
        return x, 0.0
    la = max(1, int(lookahead * SR))
    g = minimum_filter1d(g, size=2 * la + 1, mode="nearest")
    g = uniform_filter1d(g, size=la + 1, mode="nearest")
    a = np.exp(-1.0 / (release * SR))
    out = np.empty_like(g)
    y = 1.0
    for i, v in enumerate(g):  # instant attack (look-ahead already ramps it), exponential release
        y = v if v < y else v + (y - v) * a
        out[i] = y
    return x * out[:, None], float(-20 * np.log10(out.min()))


# ---------------------------------------------------------------- build
def build(cfg, stems=False):
    length = float(cfg["length"])
    n = int(round(length * SR))
    sfx_root = os.path.normpath(os.path.join(HERE, cfg["sfx_root"]))

    m = cfg["music"]
    music = decode(os.path.normpath(os.path.join(HERE, m["file"])), ss=m["start"], dur=length + 0.5)[:n]
    if len(music) < n:
        music = np.pad(music, ((0, n - len(music)), (0, 0)))
    music = fade(music, m.get("fade_in", 0.01), m.get("fade_out", 0.6))

    L, ts = short_loudness(music)
    band = (ts >= m.get("ref_from", 8.0)) & (ts < m.get("ref_to", 40.0))
    ref = float(np.percentile(L[band], 90))

    music_db = automation(m.get("automation"), n)
    sfx = np.zeros((n, 2))
    duck_db = np.zeros(n)
    report = {"ref_level_db": round(ref, 2), "cues": []}
    cache = {}

    for c in sorted(cfg["cues"], key=lambda c: c["t"]):
        path = os.path.join(sfx_root, c["file"])
        if path not in cache:
            cache[path] = decode(path)
        x = cache[path].copy()
        if "region" in c:
            a, b = c["region"]
            x = x[int(a * SR): int(b * SR)]
        if c.get("reverse"):
            x = x[::-1].copy()
        rate = c.get("rate", 1.0)
        if rate != 1.0:
            fr = Fraction(rate).limit_denominator(200)
            x = resample_poly(x, fr.denominator, fr.numerator, axis=0)
        x = filt(x, c.get("hp"), c.get("lp"))
        s = sync_point(x, c.get("sync", "peak"))
        a = 0
        b = len(x)
        if "head" in c:
            a = max(0, int((s - c["head"]) * SR))
        if "tail" in c:
            b = min(len(x), int((s + c["tail"]) * SR))
        x = x[a:b].copy()
        s -= a / SR
        fade(x, c.get("fin", 0.02 if "head" in c else 0.003), c.get("fout", 0.12 if "tail" in c else 0.01))
        lvl = level(x)
        rel = c.get("rel", KIND_REL[c.get("kind", "hit")])
        g = ref + rel - lvl
        if g > 24:
            print(f"warning: {c['file']} at {c['t']} needs {g:.1f} dB; capped at +24", file=sys.stderr)
            g = 24.0
        x = pan(x * 10 ** (g / 20), c.get("pan", 0.0))
        start = c["t"] - s
        i0 = int(round(start * SR))
        if i0 < 0:
            x = x[-i0:]
            i0 = 0
        i1 = min(n, i0 + len(x))
        sfx[i0:i1] += x[: i1 - i0]
        if c.get("duck"):  # dip the music under this cue: 15 ms in, hold, 250 ms back
            t0 = int((c["t"] - 0.015) * SR)
            hold = int(c.get("duck_hold", 0.12) * SR)
            rel_n = int(0.25 * SR)
            d = float(c["duck"])
            seg = np.concatenate([np.linspace(0, d, int(0.015 * SR)), np.full(hold, d), np.linspace(d, 0, rel_n)])
            j0, j1 = max(0, t0), min(n, t0 + len(seg))
            duck_db[j0:j1] = np.minimum(duck_db[j0:j1], seg[j0 - t0: j1 - t0])
        report["cues"].append({
            "t": c["t"], "file": c["file"], "kind": c.get("kind", "hit"), "note": c.get("note", ""),
            "sync_s": round(s, 3), "starts_at": round(start, 3), "gain_db": round(g, 1),
            "level_db": round(lvl, 1), "rel_db": rel,
        })

    music_bus = music * (10 ** ((music_db + duck_db) / 20))[:, None]
    mix = music_bus + sfx

    meter = pyln.Meter(SR)
    target = float(cfg["loudness"]["lufs"])
    ceiling = float(cfg["loudness"]["tp"]) - 0.2  # margin for the AAC encode
    gain = target - meter.integrated_loudness(mix)
    out = mix * 10 ** (gain / 20)
    gr = 0.0
    for _ in range(4):  # limit, then re-centre on the loudness target
        out, gr = limiter(out, ceiling)
        dev = target - meter.integrated_loudness(out)
        if abs(dev) < 0.05:
            break
        gain += dev
        out = mix * 10 ** (gain / 20)
    out, gr = limiter(out, ceiling)

    final = {
        "integrated_lufs": round(meter.integrated_loudness(out), 2),
        "true_peak_dbtp": round(true_peak_db(out), 2),
        "master_gain_db": round(gain, 2),
        "limiter_max_gr_db": round(gr, 2),
        "cue_count": len(cfg["cues"]),
        "cues_per_second": round(len(cfg["cues"]) / length, 2),
    }
    report["master"] = final

    dst = os.path.normpath(os.path.join(VIDEO, cfg["output"]))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    sf.write(dst, out.astype(np.float32), SR, subtype="PCM_24")
    if stems:
        sd = os.path.normpath(os.path.join(VIDEO, cfg.get("stems_dir", "../previews/qa/stems")))
        os.makedirs(sd, exist_ok=True)
        k = 10 ** (gain / 20)
        sf.write(os.path.join(sd, "music-only.wav"), (music_bus * k).astype(np.float32), SR, subtype="PCM_24")
        sf.write(os.path.join(sd, "sfx-only.wav"), (sfx * k).astype(np.float32), SR, subtype="PCM_24")
    with open(os.path.join(HERE, "mix-report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    return dst, final


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--cues", default=os.path.join(HERE, "cues.json"))
    ap.add_argument("--stems", action="store_true", help="also write music-only and sfx-only stems")
    args = ap.parse_args()
    with open(args.cues, encoding="utf-8") as f:
        cfg = json.load(f)
    dst, final = build(cfg, stems=args.stems)
    print(dst)
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
