#!/usr/bin/env bash
pkill -f "main.p[y] --listen" 2>/dev/null; sleep 3
cd ~/ComfyUI && . .venv/bin/activate
nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 &
for i in $(seq 1 90); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 2; done
curl -s http://127.0.0.1:8188/object_info > /tmp/oi.json
python3 - <<'PY'
import json
d=json.load(open("/tmp/oi.json"))
print("nodes", len(d))
for k in sorted(d):
    kl=k.lower()
    if "gguf" in kl or "flux3" in kl or "flux2" in kl or ("klein" in kl): print(" ", k)
print("CLIPLoader types has flux3:", "flux3" in d["CLIPLoader"]["input"]["required"]["type"][0])
for k in ["EmptyFlux2LatentImage","EmptyFlux3LatentImage","Flux2Scheduler","CFGGuider","SamplerCustomAdvanced","RandomNoise","KSamplerSelect","BasicScheduler"]:
    print(k, k in d)
PY
