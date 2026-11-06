#!/usr/bin/env bash
# Installs ComfyUI in WSL (user space, no sudo) and downloads SDXL base 1.0 for a first test.
set -e
export UV_HTTP_TIMEOUT=900 UV_CONCURRENT_DOWNLOADS=3 UV_HTTP_RETRIES=8
cd ~
[ -d ComfyUI ] || git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
export PATH="$HOME/.local/bin:$PATH"
[ -d .venv ] || uv venv --python 3.12 .venv
. .venv/bin/activate
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
uv pip install -r requirements.txt
mkdir -p models/checkpoints
if [ ! -f models/checkpoints/sd_xl_base_1.0.safetensors ]; then
  curl -L --fail -o models/checkpoints/sd_xl_base_1.0.safetensors \
    https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
fi
python -c "import torch;print('cuda',torch.cuda.is_available(),torch.cuda.get_device_name(0))"
echo COMFY_INSTALL_DONE
