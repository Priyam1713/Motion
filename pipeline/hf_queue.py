"""Resumable Hugging Face downloader with a work queue and N parallel streams.
    python hf_queue.py OUT_DIR STREAMS repo::path [repo::path ...]
Skips files already complete (size match from the Hub tree API). Logs to OUT_DIR/queue.log."""
import json, os, subprocess, sys, threading, queue, time, urllib.request
out, streams, items = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
os.makedirs(out, exist_ok=True)
log = open(os.path.join(out, "queue.log"), "a", buffering=1)
def say(m): log.write(time.strftime("%H:%M:%S ") + m + "\n")
sizes = {}
for repo in sorted({i.split("::")[0] for i in items}):
    d = json.load(urllib.request.urlopen(f"https://huggingface.co/api/models/{repo}/tree/main?recursive=true", timeout=60))
    for f in d:
        if f.get("type") == "file": sizes[(repo, f["path"])] = f["size"]
q = queue.Queue()
for i in items:
    q.put(tuple(i.split("::", 1)))
def worker():
    while True:
        try: repo, path = q.get_nowait()
        except queue.Empty: return
        want = sizes.get((repo, path))
        dest = os.path.join(out, repo.replace("/", "__"), *path.split("/"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if want is None: say(f"MISSING {repo}::{path}"); continue
        url = f"https://huggingface.co/{repo}/resolve/main/{path}"
        for attempt in range(80):
            if os.path.exists(dest) and os.path.getsize(dest) == want: break
            subprocess.run(["curl", "-L", "-sS", "-C", "-", "--connect-timeout", "30", "--max-time", "1500", "-o", dest, url])
        ok = os.path.exists(dest) and os.path.getsize(dest) == want
        say(("OK     " if ok else "FAILED ") + f"{repo}::{path} {want/1e9:.2f} GB")
ts = [threading.Thread(target=worker) for _ in range(streams)]
[t.start() for t in ts]; [t.join() for t in ts]
say("ALLDONE")
