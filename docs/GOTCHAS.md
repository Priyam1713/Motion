# Gotchas (symptom -> cause -> fix)

## Renderer (HyperFrames 0.9.x)
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
