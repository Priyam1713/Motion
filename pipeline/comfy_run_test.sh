#!/usr/bin/env bash
cd ~/ComfyUI && . .venv/bin/activate
nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 &
for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done
tail -4 ~/comfy_run.log
python /mnt/d/client/Motion/tools/comfy_test.py "$@"
ls -la output | tail -3
