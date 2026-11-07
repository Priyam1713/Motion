#!/usr/bin/env bash
M=/mnt/d/client/Motion/lab/models
cd ~/ComfyUI
mkdir -p models/checkpoints models/text_encoders models/clip
[ -f models/checkpoints/ltxv-2b-0.9.8-distilled.safetensors ] || cp $M/ltxv-2b-0.9.8-distilled.safetensors models/checkpoints/
[ -f models/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors ] || cp $M/t5xxl_fp8_e4m3fn_scaled.safetensors models/text_encoders/
. .venv/bin/activate
curl -s http://127.0.0.1:8188/system_stats > /dev/null || { nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 & for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done; }
python /mnt/d/client/Motion/tools/comfy_ltx_test.py "$@"
ls -la output/video | tail -3
