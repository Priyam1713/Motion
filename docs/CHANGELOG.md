# Changelog

## 2026-11-07 - Cut 5: cut 1 recreated in 16:9
- New project `video5/` (cut 4 left untouched). Cut 1's full story at 44 s, 60 fps, 1920x1080, same 180 BPM track (bars 0-29 plus the last two bars, 206 sound cues, mix -15.31 LUFS / -3.2 dBTP).
- Back from cut 1 and rebuilt: the three-step recap (01 Get your link, 02 Share responsibly, 03 Track your results), "Two levels. One link.", the KOL "You -> brand" connect line (a pulse runs the line, the mark lights on contact), the longer end card.
- New this pass: Wan 2.2 text-to-video ocean plate (Apache-2.0) behind the recap and end card; a cube-turn transition (tenth unique transition) from the recap to the KOL scene; Lucide icons.
- Not used: the Blender logo sting (flat material, still on the TODO) and FLUX 3 / MiniMax / HyperFlow (licence-limited).
- Check: 0 errors (5 lint warnings: nested media start basis, file length). Not yet listened to by the director.

## 2026-11-08 - FLUX 3 and Wan motion
- Owner accepted the FLUX 3 licence and downloaded its 3 files in a browser; moved to D:. FLUX 3 Klein nvfp4 made a 1920x1088 image in 43 s.
- ComfyUI-GGUF nodes installed with approval (clone via Windows git; WSL cannot reach github.com).
- Wan 2.2 5B with camera-move prompts: dolly clip 18.0 mean frame diff (vs 1.4), 488 s per 97 frames at 1280x704; text-to-video burst 2.9. Colour drifts from the source plate.

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

## 2026-11-07 - HyperFlow H3 Flash tested
- HyperFlow H3 Flash (Q4_K_M GGUF, 14B) image-to-video from the FLUX 3 plate: 960x544, 124 frames (5.2 s, 24 fps), 6 steps, 455 s on an RTX 5070 Ti 12 GB inside WSL (14 GB RAM cap). Mean frame difference 13.5. Colour stayed on palette for the whole clip (Wan drifted). Audio track generated (mean -30.8 dB). Licence-limited: test/internal only.
- Needed the audited ComfyUI-HyperFlow-Flash node pack (about 20 KB, no network or subprocess calls) plus ComfyUI-GGUF; installed with owner approval.

## 2026-11-07 - Qwen-Image 2.1 and MiniMax H3 NVFP4
- Qwen-Image 2.1 (int8 convrot, w4a8 Qwen3-VL 8B encoder): 1664x928, 25 steps, cfg 4, 254 s. Clean, high-contrast result, but research-only licence: test/internal only.
- MiniMax H3 NVFP4 from DeepBeepMeep (FastH3-Omni) does NOT load in ComfyUI: it is a WanGP-format file (KeyError final_layer.video_out.weight). Use WanGP on Windows for it, or Comfy-Org's own H3 files (smallest `minimax_h3_fl2va_pruned_w6a8.safetensors`, 16 GB; not downloaded).
- Two failed runs taught a rule: after another model has run, restart ComfyUI before loading the 15.7 GB H3 text encoder (cached models held 11.8 GB RAM and the load failed with HostBuffer.read_file_slice failed). `tools/comfy_restart.sh` now starts with `--fast-disk --cache-none`.
