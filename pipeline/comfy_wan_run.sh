#!/usr/bin/env bash
H=/mnt/d/client/Motion/lab/models/hub3/Comfy-Org__Wan-2.2/split_files
cd ~/ComfyUI
mkdir -p models/diffusion_models models/text_encoders models/vae
[ -f models/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors ] || cp $H/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors models/diffusion_models/
[ -f models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors ] || cp $H/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors models/text_encoders/
[ -f models/vae/wan2.2_vae.safetensors ] || cp $H/vae/wan2.2_vae.safetensors models/vae/
cp /mnt/d/client/Motion/previews/comfy/sdxl-test-01.png input/sdxl-test-01.png
. .venv/bin/activate
curl -s http://127.0.0.1:8188/system_stats > /dev/null || { nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 & for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done; }
python /mnt/d/client/Motion/tools/comfy_wan_test.py t2v "slow camera push through deep violet liquid glass waves, glowing particles drifting, cinematic lighting, smooth motion, dark background" wan_t2v 49 1280 704
python /mnt/d/client/Motion/tools/comfy_wan_test.py i2v "slow camera glide over glossy violet liquid waves, light rippling across the surface, smooth cinematic motion" wan_i2v 49 1280 704 sdxl-test-01.png
ls -la output/video
