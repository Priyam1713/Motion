#!/usr/bin/env bash
H=/mnt/d/client/Motion/lab/models/hub/black-forest-labs__flux-3-image-klein-comfy
cd ~/ComfyUI
mkdir -p models/diffusion_models models/text_encoders models/vae
for p in "diffusion_models/flux3-image-klein-nvfp4.safetensors" "text_encoders/qwen3vl_4b_int8_convrot.safetensors" "vae/flux2-vae.safetensors"; do
  [ -f "models/$p" ] || { cp "$H/$p" "models/$p.part" && mv "models/$p.part" "models/$p"; }
done
. .venv/bin/activate
curl -s http://127.0.0.1:8188/system_stats > /dev/null || { nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 & for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done; }
python /mnt/d/client/Motion/tools/comfy_flux3_test.py "$@"
