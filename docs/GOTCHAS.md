# Gotchas (symptom -> cause -> fix)

## Renderer (HyperFrames 0.9.x)
- Lint `nested_media_start_basis_ambiguous` on a `<video>` inside the film composition -> its `data-start` is read as composition-local, which is what we want (the film starts at 0 in the root); the warning is harmless here.
- **Soundtrack came out quieter than the mix** -> the renderer limits to -3 dBTP when the encoded AAC peaks above -1 dBTP -> mix at -15.3 LUFS with a -3 dBTP ceiling, then compare the master's LUFS with the WAV (`ffmpeg -i f -af ebur128=peak=true -f null -`).
- **Check/render fails on audio** -> FFmpeg/ffprobe not on PATH in that shell -> prepend FFmpeg's bin directory each session.
- **Lint: letterSpacing tween** -> not allowed -> use blur and opacity.
- **Lint: `tl.set(...,0)`** -> use `gsap.set` for initial hidden states.
- **Later tween on the same property snaps** -> `fromTo` renders immediately -> add `immediateRender:false`.
- **State swap with `tl.call` breaks on seek** -> crossfade two elements instead.
- **Words collapse in scaled containers** -> whitespace collapses -> use explicit margins on word spans.
- **One big composition**: the whole clip is live at t=0, so layout reads (`getBoundingClientRect`) are valid at build time.
- CSS `clip-path:url(#id)` with SVG polygons/text works on HTML elements; CSS masks with `--var` radii give halftone and blinds.

## Windows / shell
- A Bash tool call with a long heredoc holding quotes, backticks and `$` failed with 'unexpected EOF' -> write the script with the Write tool, then run it.
- Long Bash heredocs with non-ASCII characters or apostrophes mojibake -> write the script to a file with plain ASCII.
- Python on Windows paths -> use raw strings.
- `winget` user-scope installs often fail (no applicable installer) -> use portable zips.
- App Control can block DLLs (numba in Earshot) -> do not bypass; measure with FFmpeg instead.
- Downloads from Sonniss (Cloudflare) return 403 to scripts -> ask the human to download in a browser. Do not bypass.
- Some sites may time out on repeated loads -> retry singly.

## Blender
- Do not `transform_apply` on a 2D curve; size extrusion from the imported object's dimensions (SVG import is about 0.04 units).
- Poly Haven API: `/files/<id>` (not `/files/hdris/<id>`).
- Alpha output: render PNG RGBA, then `ffmpeg -c:v libvpx-vp9 -pix_fmt yuva420p`.

## WSL / ComfyUI
- Large PyTorch wheels can time out in `uv`: set `UV_HTTP_TIMEOUT=900 UV_HTTP_RETRIES=8` and retry.
- RTX 50-series (Blackwell) needs PyTorch built for CUDA 12.8 or newer (`cu128` index).
- **WSL cannot reach pypi.nvidia.com** (connection times out while Windows can) -> `uv pip install torch` fails on the nvidia-* wheels. Fix: on Windows run `pip download torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128 --extra-index-url https://pypi.org/simple --platform manylinux_2_28_x86_64 --python-version 3.12 --only-binary=:all: --implementation cp -d wheels`, then in WSL install with `--no-index --find-links` (see `pipeline/comfy_finish_wsl.sh`).
- **Downloads run slowly here (about 1.8 MB/s)**: a 6.9 GB model takes about an hour. Start big downloads early in the background and wait on them with a monitor instead of polling.
- GitHub pushes can time out once on this network; a plain retry worked.
- **`pip download` timed out on files.pythonhosted.org (and hung with no progress)** -> use `pip install --dry-run --report report.json --target _t --platform ... --only-binary=:all:` to resolve exact wheel URLs and hashes, then download with `pipeline/dl_urls.py` (resumable curl + sha256 check). This was far faster than pip.
- **pip --platform on Windows skips Linux-only dependencies** (torch's `cuda-toolkit`, cudnn, nccl, triton are marked `platform_system == "Linux"`) -> name them explicitly. PyPI default `torch` is not the cu128 build; pin `torch==2.11.0+cu128` from the PyTorch index.
- **Install offline wheels with `uv pip install --no-deps *.whl`**, and keep only one wheel per package (a duplicate NCCL version caused a URL conflict).
- **MSYS path conversion**: from Git Bash, call `MSYS_NO_PATHCONV=1 wsl -d Ubuntu-24.04 -- bash /mnt/d/...`; inline `bash -lc` strings with `$(...)` get mangled, so put commands in a script file.

- **WSL RAM cap**: a 97-frame 4x ESRGAN upscale at once exceeded WSL's 14 GB cap and crashed the WSL service (`Wsl/Service/E_UNEXPECTED`). Recover with `wsl --shutdown`; never raise the cap, process in chunks instead.
- **Chunked ESRGAN produced a dark 12-frame block** (frames 24-35 at about 20% brightness) in an image-to-video clip while the native clip was smooth. Always measure per-frame brightness (`signalstats` YAVG) after any batched processing. Plain Lanczos looked crisper than RealESRGAN on particle footage, so skip ESRGAN for this content.
- **Gated Hugging Face repos** (e.g. black-forest-labs FLUX 3) return 401 `GatedRepo`: the human must log in and accept the licence; do not route around the gate with third-party mirrors.
- **Killing background jobs by command-line match**: a `Get-CimInstance ... CommandLine -match 'name'` filter also matches the command that contains it and kills your own shell (exit 255). Use a bracket trick such as `hf_queu[e]`.
- **Third-party ComfyUI custom nodes run arbitrary code**: installing one (e.g. ComfyUI-GGUF) needs the owner's explicit OK.
- **Disk**: keep everything on D:. Check `Get-PSDrive C` before heavy work; pip/npm/uv caches default to C:.
- **Download speed here is about 3.3 MB/s aggregate**: order queues by priority (the model that will actually be delivered first); extra streams do not add speed.

## Models larger than RAM
- Start ComfyUI with `--fast-disk` so weights stream from disk instead of filling RAM. The 15.7 GB H3 text encoder loaded fine under the 14 GB WSL cap with this flag (about 2.5 GB RAM used). Fall back to `--async-offload` or `--lowvram` if sampling runs out of memory.
