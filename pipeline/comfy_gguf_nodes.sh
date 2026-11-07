#!/usr/bin/env bash
# Installs city96/ComfyUI-GGUF (third-party custom nodes; owner approved 2026-11-08). WSL cannot reach github.com,
# so clone with Windows git into lab/ComfyUI-GGUF first, then run this to copy it in and install its requirements.
export UV_HTTP_TIMEOUT=900 PATH="$HOME/.local/bin:$PATH"
rm -rf ~/ComfyUI/custom_nodes/ComfyUI-GGUF
cp -r /mnt/d/client/Motion/lab/ComfyUI-GGUF ~/ComfyUI/custom_nodes/
cd ~/ComfyUI && . .venv/bin/activate
uv pip install -r custom_nodes/ComfyUI-GGUF/requirements.txt 2>&1 | tail -3
ls custom_nodes
