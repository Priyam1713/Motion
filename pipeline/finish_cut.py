"""Finish and score one comparison cut the same way for every tool.
  python finish_cut.py NAME VIDEO [--audio WAV] [--gain-db -3] [--tool-notes "text"]
Steps: optional remux with our own audio (gain applied so the AAC true peak stays under -1 dBTP), measure
format, loudness, peak, near-static share, run the Earshot critique, copy to previews/cmp-NAME.mp4 and
append a row to cuts/results.json. Run with the Earshot venv python (numpy needed only for static share)."""
import argparse, json, os, re, shutil, subprocess, sys, time

ROOT = r"<project>"
ap = argparse.ArgumentParser()
ap.add_argument("name"); ap.add_argument("video")
ap.add_argument("--audio"); ap.add_argument("--gain-db", type=float, default=-3.0)
ap.add_argument("--notes", default="")
ap.add_argument("--setup-min", type=float); ap.add_argument("--render-s", type=float)
a = ap.parse_args()
out = os.path.join(ROOT, "previews", f"cmp-{a.name}.mp4")
os.makedirs(os.path.dirname(out), exist_ok=True)

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)

if a.audio:
    r = run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-i", a.audio, "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
             "-af", f"volume={a.gain_db}dB,alimiter=limit=0.83:level=false", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", out])
    if r.returncode: sys.exit(r.stderr)
else:
    shutil.copyfile(a.video, out)

pr = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate,nb_frames,duration", "-of", "json", out]).stdout)
v = next(s for s in pr["streams"] if s["codec_type"] == "video")
fr = eval(v["r_frame_rate"])
loud = run(["ffmpeg", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
lufs = float(re.findall(r"I:\s+(-?\d+\.?\d*) LUFS", loud)[-1]); peak = float(re.findall(r"Peak:\s+(-?\d+\.?\d*) dBFS", loud)[-1])
fz = run(["ffmpeg", "-i", out, "-vf", "freezedetect=n=0.0005:d=0.4", "-an", "-f", "null", "-"]).stderr
frozen = sum(float(x) for x in re.findall(r"freeze_duration: (\d+\.?\d*)", fz))
static = round(frozen / float(v["duration"]) * 100, 1)
qa = os.path.join(ROOT, "previews", "qa", f"earshot-cmp-{a.name}.json")
e = run([os.path.join(ROOT, "tools", "earshot", ".venv", "Scripts", "python.exe"), "-I", "-m", "earshot", "critique", out, "--out", qa])
ear = {}
try:
    j = json.load(open(qa)); ear = {"verdict": j.get("verdict"), "score": j.get("score"), "in_range": j.get("in_range"), "scored": j.get("scored"),
                                    "critical": (j.get("critical_issues") if isinstance(j.get("critical_issues"), int) else len(j.get("critical_issues") or [])), "major": (j.get("major_issues") if isinstance(j.get("major_issues"), int) else len(j.get("major_issues") or []))}
except Exception as ex:
    ear = {"error": str(ex)[:120]}
row = {"name": a.name, "file": out, "w": v["width"], "h": v["height"], "fps": round(fr, 2), "frames": v.get("nb_frames"),
       "duration": round(float(v["duration"]), 2), "lufs": lufs, "peak_dbfs": peak, "frozen_pct": static, "earshot": ear,
       "setup_min": a.setup_min, "render_s": a.render_s, "notes": a.notes, "when": time.strftime("%Y-%m-%d %H:%M")}
rp = os.path.join(ROOT, "cuts", "results.json")
rows = json.load(open(rp)) if os.path.exists(rp) else []
rows = [r for r in rows if r["name"] != a.name] + [row]
json.dump(rows, open(rp, "w"), indent=1)
print(json.dumps(row, indent=1))
