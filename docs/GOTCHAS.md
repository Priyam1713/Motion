# Gotchas (symptom -> cause -> fix)

## Reference analysis
- **Dot-matrix glyphs drew in a serif font** -> the canvas built its glyph grid before the web font was loaded for canvas use (`document.fonts.ready` is not enough) -> `await document.fonts.load('500 64px InterD')` for each size, and set `ctx.letterSpacing` to match the CSS.
- **CSS mask on a full-width text line hid the wrong part** -> mask percentages are relative to the 1920 px container, not the text -> compute the wipe in pixels from the measured text bounds.
- **Band glow had hard edges** -> a mask-image clips the element's own blur at its box -> blur the outer element, put the gradient and mask on an inner one.
- **The white flash frame came out grey and every hard cut became a one-frame mix** -> shutter sub-samples straddle the cut -> snap each sub-sample to the side of the cut its frame belongs to (round the frame number) before seeking.
- **A whip-zoom showed stepped copies even with 8 shutter samples** -> it moves about 700 px per frame -> add a horizontal-only SVG blur (`feGaussianBlur stdDeviation="x 0"`) scaled to camera speed, capped so words stay readable.
- **"Frozen frames" read 0% on grain** -> per-frame grain lifts every frame difference -> compare frozen share before the grain pass, or raise the threshold.
- **Tempo read as 92.9 BPM** -> a syncopated hit every 1.5 beats was taken for the beat -> fit a beat grid (librosa beat_track plus a phase fit on 16ths) and check that snares and 808s fall on fixed beat positions; the reference was 140 BPM half-time.
- **Crops of "full-res" frames came out black** -> the extracted frames were 640x360, not 1280x720 -> extract key frames straight from the video with `select=eq(n,N)`.
- **Sheets at 4 fps missed the important details** (accelerating carousel, ghost echo, rising words, self-pressing button) -> read every frame (24 per sheet) at least once.

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

## H3 NVFP4 checkpoint is WanGP-only
- `DeepBeepMeep/MiniMax-H3` files are for WanGP, not ComfyUI (KeyError `final_layer.video_out.weight`). Read the model card's target runtime before downloading 14 GB.
- Restart ComfyUI (with `--fast-disk --cache-none`) before the H3 text encoder if other models ran first, or the load fails with `HostBuffer.read_file_slice failed`.
- Python rewrites of shell scripts on Windows can add CRLF line endings and break them in WSL; run `sed -i 's/\r$//'`.

## Cut 10 build (2026-11-08)
- **Pills overlapped and the highlight drifted off the text** -> flex items shrank because the row was narrower than its content -> `flex:0 0 auto` on each pill and `width:max-content` on the row.
- **Second card sat off-centre after the flip** -> I added the first card's translation to a card that was already centred -> give each card its own origin and only share scale and z.
- **A sound effect needed +53 dB** (mixer warning "capped at +24") -> the Sonniss "Reverse Glass Effect 04" is almost silent -> pick another swell (Orbital Emitter "Searing") and re-run; read the mixer's warnings.
- **ffmpeg "moov atom not found" right after starting an encode in the background** -> the file is still being written -> wait for `ffprobe` to succeed before muxing.
- **A ghost of the big headline showed after the snap to the small line** -> a leftover dot layer reused the big glyph grid -> remove it, start the small line 0.1 s earlier so there is no blank gap.
- **Odometer sat at "00%" for two seconds** -> it rolled late -> roll it while the card pulls forward and hide the digits until the roll starts.

- (9 Nov 2026) Kokoro on Windows: `uv pip install kokoro` then the spaCy model must be installed into the venv (`en_core_web_sm` wheel) or misaki tries `uv pip` without a venv and fails; set HF_HUB_DISABLE_SYMLINKS_WARNING; write vo.json with encoding utf8 (phoneme markup has non-cp1252 characters).
- (9 Nov 2026) Openverse/Freesound foley: use `license=cc0,pdm` with 1-2 word queries (long phrases return nothing); a failed download leaves a 0-byte file, delete and retry; the Wikimedia 'LL-' results are speech, skip them; Wikimedia returns 429 if hit fast.
- (9 Nov 2026) Word timings from Kokoro tokenise spoken forms ('U S D T', 'Uni Ocean'), so look up 'at', 'ocean' etc., not 'brand' (the lookup threw and silently blanked the last scene until checked with a page-error probe, cuts/cut12/dbg.mjs).
- (9 Nov 2026) Bash tool blocks `rm` with a glob after a cd; use a fresh directory instead of clearing one.

- Kokoro lives in `.cache/kokoro-venv` (system python lacks soundfile): run `.cache/kokoro-venv/Scripts/python.exe gen_vo.py af_heart 1.08`.
- Logo mark bbox is 151x65 in the 492x66 logo viewBox (use viewBox "0 0 151 65" to place the mark alone); purple mark needs a light background to read.

- Windows Smart App Control (enforcing since 2026-11-09) blocks unsigned compiled Python modules (blis/spacy `.pyd`), so the Windows Kokoro venv no longer imports. Do not bypass; run Kokoro in WSL: `~/kokoro-venv` in Ubuntu-24.04, HF_HOME=/mnt/d/client/Motion/.cache/hf.
- CSS filter/opacity on a `preserve-3d` parent flattens its children: apply blur/fade per leaf object and blur the outer wrapper (not #cam) for transitions.
- Bloom in ffmpeg: threshold in RGB (`format=gbrp` + `lutrgb`) then `blend=addition`; thresholding only luma (lutyuv) leaves chroma and washes the whole frame purple.
