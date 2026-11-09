# To do

## Cut 12 "Every Decimal Matters" (waiting on the owner)
- [ ] Owner reads `storyboard/cut12-reference-teardown.md` and answers section 8: VO source, forecast-flow UI screenshots, logo, music-bed by ear, script open points.
- [ ] Then: one-scene test (scenes 0-1: glass lens, foley), then the full cut at 1920x1080 30 fps.

## Cut 11 reference replica
- [x] Owner approved the deep-pass report (9 Nov): Inter-like type, reference first in every aspect, logo-only silent end card, real UI from their screenshots, about 37 s.
- [x] Built cut 11 on the reference's exact frames (891 frames, 24 fps) with an original 140.6 BPM E-minor score composed to the reference's measured timeline.
- [ ] Owner's listening and viewing pass on `previews/refer-earn-cut11_reference-replica_16x9_24fps.mp4`.
- [x] Separated the reference audio (Demucs 6-stem): no separate effects layer; effects are built into the track.

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

## Cut 12 review (after build)
- [ ] Owner listens to `previews/uniocean_every-decimal-matters_cut12_16x9_30fps.mp4`: voice choice (af_heart vs another Kokoro voice), foley stand-ins (typewriter for adding machine, laid weights for brass), loudness.
- [ ] Run qa_video.py / Earshot on cut 12; fix flagged holds.
- [ ] Optional: true refraction lens (WebGL/Blender), real UI screenshots of the forecast flow to replace the rebuilt UI.

- [ ] Owner listens to cut 12 v2 (bling SFX + bed); tune levels (SFX_G, MUS_G in build_audio.py) or the kit by ear.

- Cut 13: owner listening pass and sign-off; confirm referral terms (commission base, eligibility, payout timing) with the client before publishing; replace abstract tracker with real dashboard visuals only if the feature exists.

- Cut 15: owner watch + listen pass (score balance, SFX sync feel, camera pacing). Possible upgrades: true refraction/ray-traced glass via Blender, real brand referral UI if the feature exists, mastering the bed against a reference track.
