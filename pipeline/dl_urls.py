import json, subprocess, os, hashlib, sys, time
r = json.load(open("report.json"))
os.makedirs("wheels", exist_ok=True)
for i in r["install"]:
    d = i["download_info"]; url = d["url"]; sha = d["archive_info"]["hashes"]["sha256"]
    name = url.split("/")[-1].split("#")[0]
    path = os.path.join("wheels", name)
    for attempt in range(60):
        if os.path.exists(path) and hashlib.sha256(open(path, "rb").read()).hexdigest() == sha:
            break
        subprocess.run(["curl", "-L", "-sS", "-C", "-", "--max-time", "900", "--connect-timeout", "30", "-o", path, url])
    ok = os.path.exists(path) and hashlib.sha256(open(path, "rb").read()).hexdigest() == sha
    print(name, "OK" if ok else "FAILED", flush=True)
print("ALLDONE", flush=True)
