# Tools directory

Grades: **Worked** (used in a delivered cut), **Tested** (runs, not yet in a cut), **Pending**, **Skipped** (reason given).

| Tool | Job | Licence | Grade / notes |
|---|---|---|---|
| HyperFrames 0.9.15 (Claude Code plugin) | HTML+GSAP to MP4, lint/check/snapshot/render | see plugin | **Worked.** Main engine. Run through `plugin-cli.mjs` |
| Remotion 4.0.x | React-based video, second engine | Free for individuals / small companies, company licence above that (confirmed eligible by the owner, 7 Nov 2026) | **Tested.** 90-frame 1080p60 render OK (`lab/remotion-test`). Use when a React component library or data-driven template suits |
| GSAP | Timelines inside compositions | GSAP standard licence | **Worked** |
| FFmpeg 9.0.1 (+ libvmaf) | Encode, loudness, analysis | LGPL/GPL | **Worked.** Always on PATH |
| puppeteer-core + chrome-headless-shell | Real site screenshots | Apache-2.0 / BSD | **Worked** |
| Blender 4.5 LTS (portable, Cycles + OptiX) | 3D logo sting with alpha | GPL (renders are ours) | **Tested.** `pipeline/blender/logo_sting.py`; material and geometry need polish |
| Poly Haven HDRIs | Blender lighting | CC0 | **Tested** |
| Lucide icons | Icon set | ISC | **Tested** |
| Earshot (critique) | Automated video+audio critique | MIT | **Worked** (22/23 on cut 4). Blocked later by Windows App Control (numba DLL); not bypassed |
| librosa, PySceneDetect, pyloudnorm, soundfile | Beat, scene and loudness analysis | ISC/BSD/MIT | **Tested** |
| OpenCV (ORB similarity, Laplacian) | Per-frame camera scale, edge vs centre sharpness, vignette, grain | Apache-2.0 | **Worked 9 Nov 2026.** Text-only frames give noisy ORB scale; measure text bounding boxes there instead |
| audio-separator (UVR models) | Split a reference mix into stems | MIT (models vary) | **Worked 9 Nov 2026.** `tools/sep-venv` (CUDA torch); htdemucs_6s splits 37 s in 12 s on the RTX 5070 Ti. Needed `audioread` installed by hand. No dialogue/music/effects model in its catalogue |
| Inter 4.1 (rsms/inter release zip) | Film type for cut 11 (Inter Display Medium for titles) | SIL OFL 1.1 | **Worked 9 Nov 2026.** Closest free match to the reference's neo-grotesque; the UI keeps the site's Lato |
| numpy + scipy score synthesis (`cuts/cut11/build_music.py`) | Original music composed to a measured timeline (808, snare/clap, hats, pads, plucks, pitched UI pings, riser, reverse swell) | ours | **Worked 9 Nov 2026.** Gives frame-exact sync with no licence risk; tempo and key measured back as 140.6 BPM E minor. Needs the owner's ear for balance |
| Audacity 4 (portable) | Audio inspection | GPL | **Tested** |
| ComfyUI + LTX-Video 2B 0.9.8 distilled | Local text-to-video for background plates | LTX Video open-weights licence (check terms for commercial use before using in a delivered film) | **Tested 7 Nov 2026.** 768x448, 97 frames (4 s at 24 fps), 8 steps, cfg 1, 73.7 s on the RTX 5070 Ti. Result: coherent glowing particle waves with gentle camera drift; motion is subtle, resolution needs upscaling (1080p) before use. Files: `ltxv-2b-0.9.8-distilled.safetensors` (6.3 GB) + `t5xxl_fp8_e4m3fn_scaled.safetensors` (5.2 GB); scripts `pipeline/comfy_ltx_run.sh`, `pipeline/comfy_ltx_test.py` |
| ComfyUI (WSL, CUDA 12.8) | Local image/video generation | GPL-3.0; each model has its own licence | **Tested 7 Nov 2026.** SDXL base 1.0 text-to-image works on the RTX 5070 Ti (PyTorch 2.11 cu128): 1344x768, 25 steps, 239 s for the first run including model load. Abstract violet-glass waves looked usable as a background plate. Next: LTX-Video / Wan for motion |
| MiniMax H3 / HyperFlow H3 Flash | Best open-weight video (per Arena); H3 community licence excludes outputs shown in US/EU/UK/Korea | Test only; see LICENCE note | **Downloading for tests 7 Nov 2026** |
| Wan 2.2 TI2V-5B | Apache-2.0 video model, the safest licence | Apache-2.0 | **Tested 8 Nov 2026 (cleared for delivery).** Native 1280x704, 49 frames (2 s at 24 fps), 20 steps uni_pc cfg 5 shift 8: text-to-video 298 s, image-to-video 237 s on the RTX 5070 Ti 12 GB (first run includes model load). Much better look than LTX 2B (clean glass waves, stable brightness, no artifacts) but motion is gentle; try longer prompts about camera movement, more frames, and the fp8 UNet for speed. Scripts `pipeline/comfy_wan_run.sh`, `pipeline/comfy_wan_test.py` | **Used in a film 7 Nov 2026 (cut 5):** the t2v burst clip, cropped to 16:9, interpolated to 60 fps (ffmpeg minterpolate) and ping-pong looped, works as a dimmed background plate; use it under a dark gradient, not as a hero shot.
| FLUX 3 Image Klein (nvfp4) | Best local image model tested | Gated on Hugging Face (owner accepted; read terms before any delivered use) | **Tested 8 Nov 2026.** Native 1920x1088, 4 steps, cfg 1, euler + Flux2Scheduler, 43 s on the RTX 5070 Ti (NVFP4 runs natively on Blackwell). Sharp, cinematic depth of field; clearly beats SDXL. Needs `UNETLoader` + `CLIPLoader type flux3` (qwen3vl_4b) + `flux2-vae`; scripts `pipeline/comfy_flux3_*` |
| ComfyUI-GGUF custom nodes (city96) | Load GGUF models (HyperFlow) | Third-party code, installed with the owner approval 8 Nov 2026 | Installed; WSL cannot reach github.com, so clone with Windows git and copy in |
| Qwen-Image 2.1 (still downloading) | Newest open image models | Qwen: research-only. FLUX 3: gated, user must accept | Qwen downloading; FLUX waiting on user |
| DaVinci Resolve (free) | Human listening pass, grading, final polish | Blackmagic EULA | **Pending.** Needs admin install by the owner: https://www.blackmagicdesign.com/products/davinciresolve |
| Inkscape, Krita | Vector / paint | GPL | **Skipped** (installer needs admin) |

## Looked at, not installed
Motion Canvas, Three.js, Lottie tooling, TTS engines, generative video models: evaluate only against a concrete shot.

| Subframe Motion MCP / HyperFrames `reverse` | Motion examples; reverse-engineer a video into HTML | MIT examples / Pro feature | **Skipped for the reverse:** HyperFrames `reverse start` is a Pro (paid) feature, so the breakdown was done with ffprobe, numpy and our own sheets instead. No spend. |
| Cut 10 engine (`cuts/cut10/film.src.html`, `render_seek.mjs`, `tmix`) | Pure-function-of-time HTML film, sub-frame blur | MIT (our own) | **Worked.** 48 s at 1080p60 in about 5 min. |

## Cut 12 (9 Nov 2026)
- Kokoro-82M (`af_heart`, CPU, Apache-2.0): worked; natural warm female read, word timestamps; pronunciation of 'brand' fixed with a phoneme override. Listening pass by the owner pending.
- Openverse API (CC0 Freesound previews): worked for cards, glass, typewriter, domino, toggle, hole punch, stamp, printers, clicker, ratchet, keys, latch; partly for brass weight and abacus (stand-ins: laid weights, wooden clacks); no CC0 adding-machine key or label maker found.
- Chrome seek renderer + tmix (cuts/_tools/render_seek.mjs): worked, 50 captures/s on 3 workers.
