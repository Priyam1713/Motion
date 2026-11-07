#!/usr/bin/env bash
# Installs the audited HyperFlow node pack (owner approved), links models, restarts ComfyUI with --fast-disk, runs the i2v test.
M=/mnt/d/client/Motion/lab/models/hub3
C=~/ComfyUI
rm -rf $C/custom_nodes/ComfyUI-HyperFlow-Flash
cp -r /mnt/d/client/Motion/lab/ComfyUI-HyperFlow-Flash $C/custom_nodes/ && rm -rf $C/custom_nodes/ComfyUI-HyperFlow-Flash/.git
mkdir -p $C/models/diffusion_models $C/models/text_encoders $C/models/vae $C/input
ln -sf $M/VideoRebirthAI__hyperflow-h3-flash/fl2va_gguf/*.gguf $C/models/diffusion_models/
ln -sf $M/Comfy-Org__MiniMax-H3/text_encoders/*.safetensors $C/models/text_encoders/
ln -sf $M/Comfy-Org__MiniMax-H3/vae/*.safetensors $C/models/vae/
cp /mnt/d/client/Motion/previews/comfy/flux3-test-01.png $C/input/
pkill -f "main.p[y] --listen" 2>/dev/null; sleep 4
cd $C && . .venv/bin/activate
nohup python main.py --listen 127.0.0.1 --port 8188 --fast-disk > ~/comfy_run.log 2>&1 &
for i in $(seq 1 90); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 2; done
free -g | head -2
python /mnt/d/client/Motion/tools/comfy_hyperflow_test.py "The camera dollies fast and low forward over the dark violet sea toward the glowing horizon, waves surge and spray flies past, cinematic, motion-heavy, same violet colour palette" hyperflow/i2v-test flux3-test-01.png "$@"
