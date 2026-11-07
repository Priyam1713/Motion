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
| Audacity 4 (portable) | Audio inspection | GPL | **Tested** |
| ComfyUI + LTX-Video 2B 0.9.8 distilled | Local text-to-video for background plates | LTX Video open-weights licence (check terms for commercial use before using in a delivered film) | **Tested 7 Nov 2026.** 768x448, 97 frames (4 s at 24 fps), 8 steps, cfg 1, 73.7 s on the RTX 5070 Ti. Result: coherent glowing particle waves with gentle camera drift; motion is subtle, resolution needs upscaling (1080p) before use. Files: `ltxv-2b-0.9.8-distilled.safetensors` (6.3 GB) + `t5xxl_fp8_e4m3fn_scaled.safetensors` (5.2 GB); scripts `pipeline/comfy_ltx_run.sh`, `pipeline/comfy_ltx_test.py` |
| ComfyUI (WSL, CUDA 12.8) | Local image/video generation | GPL-3.0; each model has its own licence | **Tested 7 Nov 2026.** SDXL base 1.0 text-to-image works on the RTX 5070 Ti (PyTorch 2.11 cu128): 1344x768, 25 steps, 239 s for the first run including model load. Abstract violet-glass waves looked usable as a background plate. Next: LTX-Video / Wan for motion |
| DaVinci Resolve (free) | Human listening pass, grading, final polish | Blackmagic EULA | **Pending.** Needs admin install by the owner: https://www.blackmagicdesign.com/products/davinciresolve |
| Inkscape, Krita | Vector / paint | GPL | **Skipped** (installer needs admin) |

## Looked at, not installed
Motion Canvas, Three.js, Lottie tooling, TTS engines, generative video models: evaluate only against a concrete shot.
