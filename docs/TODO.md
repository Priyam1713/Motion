# To do

## Next
- [x] ComfyUI SDXL smoke test passed.
- [x] LTX-Video 2B distilled text-to-video smoke test passed.
- [x] Wan 2.2 TI2V-5B t2v and i2v tests passed.
- [ ] Wan 2.2: push motion (camera-move prompts, 97+ frames, 1080p), time fp8 vs fp16, try Wan2.2 A14B GGUF if quality justifies the time.
- [ ] ComfyUI: upscale an LTX clip to 1080p (LTX spatial upscaler or ffmpeg), try image-to-video from an SDXL plate, compare Wan 2.x, time a second SDXL run.
- [ ] Remotion: port one scene to compare authoring speed with HyperFrames.
- [ ] Index the Sonniss GameAudioGDC 2024 bundles once downloaded (librosa: duration, loudness, onset), tag by use (UI, impact, riser, ambience).
- [ ] Blender: improve the logo material (less matte) and fix the inner-edge gap; try a shorter, punchier sting.
- [ ] Replace Content-ID-flagged music with a clear track (decision pending).
- [ ] Scene-level VMAF / frozen-frame checks wired into one `qa` script.

## Needs a human
- [ ] Accept the FLUX 3 licence on Hugging Face and place the three files (owner is downloading them in the browser).
- [ ] Approve installing ComfyUI-GGUF custom nodes (third-party code) so HyperFlow GGUF can load.
- [ ] Download Sonniss bundles into `assets/audio/sfx/sonniss/`.
- [ ] Install DaVinci Resolve (admin) for the listening pass.
- [ ] Client sign-offs: wording, rates, permission to show real UI.

## Later cuts
Only after the toolkit is maxed out. No new cut until the director asks.
