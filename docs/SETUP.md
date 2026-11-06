# Replicate the setup

Target: Windows 11, NVIDIA GPU (tested on RTX 5070 Ti Laptop, 12 GB), WSL2 Ubuntu 24.04. No admin rights needed for anything here except DaVinci Resolve.

1. **Node.js 24**, **Python 3.12**, **Git**, **FFmpeg** (winget `Gyan.FFmpeg.Essentials`, then put its `bin` folder on PATH).
2. **Claude Code** with the **HyperFrames plugin**. Set `HYPERFRAMES_NO_TELEMETRY=1`.
3. Run `scripts/bootstrap.ps1` (downloads portable Blender and Audacity, creates the Python analysis env).
4. **Remotion** (optional second engine): `npm install` in a folder with `remotion`, `@remotion/cli`, `react`, `react-dom` pinned to one version; render with `npx remotion render`.
5. **ComfyUI** in WSL: `wsl bash pipeline/install_comfy_wsl.sh`, then start with `cd ~/ComfyUI && . .venv/bin/activate && python main.py --listen 127.0.0.1`.
6. Build and render the example film with the commands in each pipeline script's header.

Everything downloaded goes in its own folder; scripts are kept elsewhere. Run Python with `-I` when it reads downloaded files.
