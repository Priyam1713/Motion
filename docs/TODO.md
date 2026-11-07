# To do

## Next
- [x] ComfyUI SDXL smoke test passed.
- [x] LTX-Video 2B distilled text-to-video smoke test passed.
- [x] Wan 2.2 TI2V-5B t2v and i2v tests passed.
- [x] Wan 2.2 motion push done (dolly i2v from FLUX plate: strong motion).
- [ ] Wan 2.2: colour-lock the drift (prompt for "deep violet only"), try 1080p, fp8 UNet speed, A14B GGUF; and (camera-move prompts, 97+ frames, 1080p), time fp8 vs fp16, try Wan2.2 A14B GGUF if quality justifies the time.
- [ ] ComfyUI: upscale an LTX clip to 1080p (LTX spatial upscaler or ffmpeg), try image-to-video from an SDXL plate, compare Wan 2.x, time a second SDXL run.
- [ ] Remotion: port one scene to compare authoring speed with HyperFrames.
- [ ] Index the Sonniss GameAudioGDC 2024 bundles once downloaded (librosa: duration, loudness, onset), tag by use (UI, impact, riser, ambience).
- [ ] Blender: improve the logo material (less matte) and fix the inner-edge gap; try a shorter, punchier sting.
- [ ] Replace Content-ID-flagged music with a clear track (decision pending).
- [ ] Scene-level VMAF / frozen-frame checks wired into one `qa` script.

- [ ] Cut 5: director review of `previews/refer-earn-cut5_16x9_60fps.mp4`; check the splice at bar 30 (film 40.0 s) by ear.
- [ ] Cut 5: build a `previews/review-cut5` page like cut 4's.
- [ ] Cut 6 (cut 1 exact, 16:9): director review of `previews/refer-earn-cut6_16x9_60fps.mp4`; owner to confirm the 16:9 re-layouts keep what they liked.

## Needs a human
- [ ] Listen to cut 5 (music splice at 40.0 s, sound audibility) and give notes.
- [ ] Download Sonniss bundles into `assets/audio/sfx/sonniss/`.
- [ ] Install DaVinci Resolve (admin) for the listening pass.
- [ ] Client sign-offs: wording, rates, permission to show real UI.

## Later cuts
Only after the toolkit is maxed out. No new cut until the director asks.

## After cut 10 (2026-11-08)
- [ ] Owner: listen to cut 10 (mix only measured by us), approve or mark up.
- [ ] Owner: confirm rates (script 15% / 10% vs docs example 10% / 5%) and permission to show real UI (C1, C9).
- [ ] Owner: approve every on-screen line in `storyboard/cut10-beat-sheet.md` and the KOL role cards (KOL, Influencer, Creator, Educator, Community lead, Analyst, Podcaster, Publisher).
- [ ] Check Content ID on Mixkit "Electro Dreams"; if flagged, swap the track (structure needs 8 quiet bars then a pulse).
- [ ] If approved: portrait 9:16 and 1:1 versions; captions for muted autoplay.
