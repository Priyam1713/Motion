#!/usr/bin/env bash
# Second half of the ComfyUI install, for networks where WSL cannot reach pypi.nvidia.com:
# PyTorch wheels are downloaded on Windows into lab/wheels first (pip download ... --platform manylinux_2_28_x86_64).
set -e
export UV_HTTP_TIMEOUT=900 UV_HTTP_RETRIES=8 PATH="$HOME/.local/bin:$PATH"
cd ~/ComfyUI
[ -d .venv ] || uv venv --python 3.12 .venv
. .venv/bin/activate
uv pip install --no-index --find-links /mnt/d/client/Motion/lab/wheels torch torchvision torchaudio
uv pip install -r requirements.txt
mkdir -p models/checkpoints
[ -f models/checkpoints/sd_xl_base_1.0.safetensors ] || cp /mnt/d/client/Motion/lab/models/sd_xl_base_1.0.safetensors models/checkpoints/
python -c "import torch;print('cuda',torch.cuda.is_available(),torch.cuda.get_device_name(0),torch.__version__)"
echo COMFY_FINISH_DONE
