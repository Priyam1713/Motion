# What works (with numbers)

## Studying a reference
- **Same timeline as the reference** (cut 11): building on the reference's exact frame numbers makes every comparison like-for-like: one script pulls both films at the same frame and the per-frame measurements line up shot by shot.
- **Composing the score in code** on the measured beat grid gives frame-exact sync and no licence risk; tempo and key measure back exactly (140.6 BPM, E minor).
- **Per-shot camera check**: measure camera scale per shot for both films. Cut 11's first render was 5-30x too static in the UI shots; raising push, pull and scroll speeds took the median from 0.08% to 0.32% per frame (reference 0.44%).
- Read **every frame** on labelled 24-frame sheets, then measure: edge vs centre sharpness (Laplacian per unit gradient), vignette, frozen-frame share, camera scale per frame, and per-hit sound character. Running the same script on our own cut turns "feels off" into numbers (e.g. frozen 6% vs 20%, camera scale change 0.44% vs 0.03% per frame).

| Technique | Result |
|---|---|
| Real captured product imagery (headless Chrome) | Biggest visual upgrade between cuts 3 and 4 |
| 180 BPM drum and bass, edited on bar lines (bar = 1.3334 s) | Reads as fast and upbeat; scene changes land on bars |
| SFX placed 1-10 dB under music with 2 dB ducking | 156 of 183 cues within 6 dB of the music (audible); cut 3 was 13-20 dB under (inaudible) |
| Nine distinct transitions in one composition | Portal, SVG text mask, 3D flip, feTurbulence ripple, freeze + shatter, halftone, pixel grid, blinds, barn doors |
| Freeze (grayscale + chromatic aberration) then shatter on the drop | The "shock" the director asked for |
| Continuous slow camera pushes on holds | Frozen frames 16.3% -> 5.9% (longest 0.33 s); references run 2-33% |
| Mix at -15.3 LUFS / -3 dBTP | Renderer left the track untouched; master measured -15.4 LUFS |
| Blender Cycles + OptiX on an RTX 5070 Ti Laptop | About 12 s/frame at 1080p for a glossy 3D logo with alpha |
| Wan 2.2 5B image-to-video from a FLUX 3 plate with a camera-move prompt ("dollies forward fast and low... swells roll toward the lens") | Mean frame difference 18.0 vs 1.4 for the first gentle prompt (about 13x more motion); 97 frames, 1280x704, 488 s. It drifts from the plate colour (violet to pink-white spray), so keep prompts specific about colour. Prompt the camera and the physics explicitly; "slow, smooth, gentle" prompts give almost static video |
| FLUX 3 Klein for stills | 1920x1088 in 43 s, 4 steps |
| Remotion 4 (React) | Installed and rendered a 90-frame 1080p60 test in under a minute on this PC |

## HyperFlow H3 Flash i2v (tested 2026-11-07, test-only licence)
- Q4_K_M GGUF + 32B NVFP4 text encoder + H3 video/audio VAEs, `HyperFlowSigmas` 6 steps, euler, BasicGuider (no CFG).
- 960x544 x 124 frames: 455 s, motion 13.5, palette held, native audio. Best colour fidelity so far among the video models tested.
- Script: `tools/comfy_hyperflow_run.sh` and `tools/comfy_hyperflow_test.py`.
| Cut 5: cut 1 recreated in 16:9 on cut 4's engine (copy the project, patch the source, reuse the cue builder) | 44 s, 1920x1080, 60 fps, 206 cues, -15.3 LUFS; check 0 errors; render 6 min 28 s (71 MB) |
| Cut 6: porting a 9:16 film to 16:9 by keeping each scene's timeline and re-laying only coordinates (scene sources in `src/`, `build.py` fills the logo paths); reusing the original mixed wav so music and SFX stay identical | 43 s, 1920x1080, 60 fps, check 0 errors; the original per-scene timings carry over untouched |
| Wan 2.2 t2v clip as a dimmed background plate (crop to 16:9, minterpolate to 60 fps, ping-pong loop to 8 s) under a dark gradient | Adds depth to the recap and end card without competing with type |
| Cube-turn transition (perspective on the root, both scenes rotate about an axis 960 px behind the frame) | Tenth unique transition, 2 tweens |

## Qwen-Image 2.1 t2i (tested 2026-11-07, research-only licence)
- UNETLoader int8_convrot + CLIPLoader type `qwen_image` (qwen3vl_8b_w4a8) + ModelSamplingAuraFlow shift 3.1 + KSampler euler/simple 25 steps cfg 4. 1664x928 in 254 s. Script: `tools/comfy_qwen21_test.py`.

## Verdict on HyperFlow output (owner listening, 2026-11-07)
- Generated audio: dull, hard to listen to at full volume, attempted ocean sound not usable. Do not use generated audio; mix real SFX (Sonniss etc.) instead.
- Image-to-video: motion smooth, but image quality is not high. Treat as look-development / motion reference, not final pixels.

## Generated-plate film (cut 7, 2026-11-07)
- Four FLUX 3 stills (45 s each) plus three Wan 2.2 i2v clips (about 8 minutes each) were enough plates for a 32 s dark-ocean film when layered with type, real UI cards and slow zooms. Prompt the motion explicitly and add colour-lock wording ("keep the same violet and navy colour palette") to hold the palette.
- Transition recipes that rendered cleanly in HyperFrames: circle clip-path iris, conic-gradient mask clock wipe (animate a CSS variable angle), polygon clip-path with a sine wave edge, SVG clipPath rects for zipper bars, radial-gradient mask ink drop, diagonal polygon sweep with a seam bar.

## Reference-driven cut (cut 10, 2026-11-08)
- Measure the reference before designing: per-frame difference found the single white flash frame (28.17 s) and every dense burst; band-split onsets showed the sound lands 40-60 ms after the picture event and that the hit leads the flash by one frame.
- One engine for all motion: `window.seek(t)` as a pure function of time plus sub-frame blending (4 sub-frames, `tmix`) rendered the whole 48 s film in about 5 minutes and made the flip and dissolves look filmic.
- Dot-matrix dissolve as the universal connector: a CSS mask wipe on the element plus a canvas of dots near the wipe edge (glyph-shaped for text, rect-shaped for cards) replaced hard cuts in six places.
- Rack focus by blurring and darkening only the base plane while the featured card moves forward in the same 3D context.
- Odometer cues computed from the picture's easing curve (inverse of ease-out cubic) keep every digit tick exactly on the digit change.
- Pick music by structure, not genre: "Electro Dreams" has 8 bars of quiet bed then a pulse, which matches the reference's quiet-then-pulse shape; offset by the measured kick phase (8.1 s) so the first kick lands on the key visual.

- (9 Nov 2026) Magnifier as a cloned DOM: `cloneNode(true)` of the whole animated world, scaled and translated inside a circular overflow:hidden glass, gives a true magnifier on live text and UI for any frame in `seek(t)`; a `.rv` rule makes title words visible inside the lens before the world reveals them (title is revealed by the lens). Row reorders as a sum of eased rank deltas (`pos = r0 + sum(delta * ease(t - te))`) never overlap rows or jump when two changes are close.
- (9 Nov 2026) Subtitle-strip pixel diff at 30 fps recovers voice-over timing from a finished video with no speech-to-text model.
- (9 Nov 2026) Kokoro af_heart per-sentence clips with word timestamps drive both the picture (landing a number on the word 'hundred') and the subtitles.
