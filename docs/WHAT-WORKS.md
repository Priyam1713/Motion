# What works (with numbers)

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
