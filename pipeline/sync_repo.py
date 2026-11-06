r"""Copy the public-safe parts of the working project into the Motion GitHub repo, commit, and optionally push.

    python tools/sync_repo.py            # copy + commit
    python tools/sync_repo.py --push     # copy + commit + push

Whitelist only: client documents, brand files, product screenshots, downloaded media and renders are never copied.
The repo clone lives at D:\client\Motion-repo (created on first run).
"""
import argparse, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
DST = os.path.join(os.path.dirname(SRC), "Motion-repo")
REMOTE = "https://github.com/Priyam1713/Motion.git"

# (source relative to project, destination relative to repo)
COPY = [
    ("repo-docs", "."),
    ("video/audio/mix.py", "pipeline/audio/mix.py"),
    ("video/blender/logo_sting.py", "pipeline/blender/logo_sting.py"),
    ("tools/install_comfy_wsl.sh", "pipeline/install_comfy_wsl.sh"),
    ("tools/comfy_finish_wsl.sh", "pipeline/comfy_finish_wsl.sh"),
    ("tools/comfy_test.py", "pipeline/comfy_test.py"),
    ("tools/sync_repo.py", "pipeline/sync_repo.py"),
    ("lab/remotion-test/package.json", "pipeline/remotion-test/package.json"),
    ("lab/remotion-test/tsconfig.json", "pipeline/remotion-test/tsconfig.json"),
    ("lab/remotion-test/src", "pipeline/remotion-test/src"),
]
SANITIZE = [  # (regex, replacement) applied to copied text files
    (r'r"C:[^"]*"\s*r"[^"]*"\s*r"[^"]*ffmpeg.exe"', 'r"ffmpeg.exe"'),
    (r"Refer & Earn", "example film"),
    (r"UniOcean", "brand"),
    (r"uniocean-mark\.svg", "brand-mark.svg"),
    (r"D:.{1,3}client.{1,3}Motion", "<project>"),
]
TEXT = (".py", ".md", ".sh", ".ps1", ".json", ".ts", ".tsx")

def run(*a, cwd=DST):
    return subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True).stdout

def copy_file(s, d):
    os.makedirs(os.path.dirname(d), exist_ok=True)
    if s.endswith(TEXT) and not s.endswith("sync_repo.py"):
        t = open(s, encoding="utf-8").read()
        for pat, rep in SANITIZE:
            t = re.sub(pat, rep, t)
        open(d, "w", encoding="utf-8", newline="\n").write(t)
    else:
        shutil.copy2(s, d)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--push", action="store_true"); ap.add_argument("-m", default="Update toolkit after pass")
    a = ap.parse_args()
    if not os.path.isdir(os.path.join(DST, ".git")):
        subprocess.run(["git", "clone", REMOTE, DST], check=True)
    for s, d in COPY:
        sp, dp = os.path.join(SRC, s), os.path.normpath(os.path.join(DST, d))
        if os.path.isdir(sp):
            for r, _, fs in os.walk(sp):
                if "node_modules" in r or "out" in r.split(os.sep):
                    continue
                for f in fs:
                    copy_file(os.path.join(r, f), os.path.join(dp, os.path.relpath(os.path.join(r, f), sp)))
        elif os.path.exists(sp):
            copy_file(sp, dp)
        else:
            print("missing:", s)
    open(os.path.join(DST, ".gitignore"), "w").write("node_modules/\nout/\n*.mp4\n*.wav\n*.mp3\n*.blend\n.venv/\n")
    run("git", "add", "-A")
    if not run("git", "status", "--porcelain").strip():
        print("nothing to commit"); return
    msg = a.m + "\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
    run("git", "commit", "-m", msg)
    print(run("git", "log", "--oneline", "-1"))
    if a.push:
        run("git", "push", "-u", "origin", "HEAD")
        print("pushed")

main()
