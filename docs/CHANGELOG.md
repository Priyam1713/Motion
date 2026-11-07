# Changelog

## 2026-11-08 - Wan 2.2 TI2V-5B tested
- Wan 2.2 5B produced clean 1280x704 clips natively (t2v 298 s, i2v 237 s, 49 frames); brightness stable, no artifacts; visibly better than LTX 2B. Motion is subtle. Apache-2.0, so it is the delivery model. Copying 10 GB from /mnt/d into WSL takes about 15 min: copy once.

## 2026-11-07 - Newer models queued, licence split
- Owner research found FLUX 3 Klein, Qwen-Image 2.1, MiniMax H3, HyperFlow H3 Flash and Wan 2.2 outclass SDXL/LTX-2B. Rule added: always use the best available.
- Licence split agreed: licence-limited models (H3/HyperFlow: no display in US/EU/UK/Korea; Qwen-Image research-only; FLUX 3 gated) for tests only; Wan 2.2 (Apache-2.0) for delivered work.
- LTX 4x chunked ESRGAN upscale to 1080p took 290 s but looked softer than Lanczos and one chunk came out dark; image-to-video from an SDXL plate worked natively.
- C: drive ran low; everything now lives on D:.

## 2026-11-07 - LTX-Video test
- LTX-Video 2B distilled generated a 4 s 768x448 clip in 73.7 s (8 steps). Looks like a usable abstract background plate; needs upscaling and a motion/quality comparison with Wan 2.x. Model downloads took about 1 hour at ~3 MB/s combined.

## 2026-11-07 - ComfyUI working
- ComfyUI + SDXL base 1.0 generated its first image (239 s incl. model load). Fix chain is in GOTCHAS (WSL cannot reach pypi.nvidia.com; pip download kept timing out; a resumable curl downloader with hash checks fixed it).

## 2026-11-07 - Toolkit pass
- Created this repo structure and the update-every-pass rule.
- Remotion 4 installed and verified (90-frame 1080p60 test render).
- ComfyUI cloned in WSL (venv created). Install blocked: WSL times out on pypi.nvidia.com, so PyTorch wheels and the SDXL base checkpoint are downloading on the Windows side (about 1.8 MB/s). Smoke test (`pipeline/comfy_test.py`) not yet run.
- Repo created and pushed; `tools/sync_repo.py` copies only whitelisted, sanitised files.
- Resolve install guidance given (admin required, owner installs).

## 2026-11-06 - Cut 4 approved
- 34 s, 180 BPM, nine unique transitions, real site imagery, audible SFX; mixed -15.3 LUFS. Details in WHAT-WORKS.
- After cut 4: Blender 4.5 + OptiX logo sting, Poly Haven HDRIs, Lucide, 23 CC0 SFX, Audacity, analysis venv.

## 2026-11-04..06 - Cuts 1-3
- Cut 1 rejected (slow, node diagrams). Cut 2 approved with notes. Cut 3 rejected (SFX inaudible, slow feel, repeated transitions, limited assets). Lessons are in DOS-AND-DONTS.
