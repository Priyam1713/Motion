# Changelog

## 2026-11-09 - Cut 12 v2: bling / token SFX and a calm music bed (picture unchanged)
- Owner feedback: the foley version read as whooshes and slams; the reference's sounds are catchy, bling/token/arcade. Stem-separated the reference (htdemucs_6s) and measured it: the non-voice layer is mostly short broadband ticks plus a few tonal pings (about 2 kHz at 14.8 s as the counter lands, 4.6-4.9 kHz sparkles, 2.6 kHz on the logo at 93.9 s); no music bed.
- Replaced all foley with a synthesized kit (`cuts/cut12/build_audio.py`): FM bells, 25% pulse coin (note then perfect-fourth jump), pitched blips, marimba plucks, sparkle arpeggios, thumps only as a soft weight under a bell; all in C major pentatonic. 160 cues (22 new cue types such as `land`, `lock`, `rank1`, `full`, `bling`, `word` added in the scene JS without changing a pixel). Added an original calm upbeat bed (100 BPM, C-G-Am-F, e-piano, pad, plucks, light kick/hat/rim, outro hold) ducked 55% under the voice.
- Levels: voice -15.9 LUFS stem, SFX stem about -22, music stem -26; mix -16.0 LUFS, -1.5 dBTP. Output `previews/uniocean_every-decimal-matters_cut12_v2_sfx-music_16x9_30fps.mp4` (video stream copied from v1). Not yet listened to.

## 2026-11-09 - Cut 12 "Every Decimal Matters" built (87 s, 1920x1080, 30 fps)
- Approved by the owner after the teardown; follows the revised script (BTC, 110K-60K scale bar, YOU rank sequence #4,#2,#5,#3,#1,#2,#1, tie-break timestamp, log index, block number, 51% / 70%, 1,000 to 100,000 entries, EVENT NOT FULL, 0.01 lens to logo). Fixes the reference's contradictions (settled list, capacity bar, garbled title morph).
- Build: one deterministic `seek(t)` HTML page (`cuts/cut12/index.html` + `film.js`, `s4.js`, `s5.js`, `s6.js`), Chrome frame capture with 4 sub-frames per frame and tmix (10,440 captures in about 3.5 min), glass lens = magnified clone of the live world inside a clipped circle (real magnification of whatever is under it, SVG rim, handle, specular). Rank list, pins and live line all computed from one price path so the abacus cues land on every real rank change (`window.CUES` dumped to `cues.json` is the single source for sound timing).
- Voice: Kokoro af_heart (female, Apache-2.0) at speed 1.06, sentence clips with word timings; 65.5 s of speech; subtitles burned in. Foley: 39 CC0 Freesound clips (cards, glass slide, typewriter key, domino, toggle, weights, wooden clacks, hole punch, stamp, receipt/label printer, clicker, ratchet, keys, latch) placed by cue; no music, no ka-ching/whoosh. Mix -16.0 LUFS, -1.5 dBTP, SFX stem peaks about 6 dB under the voice.
- Output `previews/uniocean_every-decimal-matters_cut12_16x9_30fps.mp4` (87.0 s). Not yet listened to; not yet run through qa_video / Earshot.

## 2026-11-09 - Cut 11 "Reference replica" (example film)
- Owner approved the deep-pass report: Inter-like type, the reference first in every aspect, logo-only silent end card, real brand UI (owner's own screenshots of the signed-in example film page plus the public homepage), about 37 s.
- The reference's own music could not be used (third-party recording, no published credit or licence). Instead composed an original score in code on the reference's measured timeline: 140.6 BPM half-time, E minor, 808 drop at 7.08 s, snares on the snap re-frames, stutters, choke after the white frame, silence, reverse swell into a sub boom on the URL. Effects are part of the score (same key and drum palette), as the reference's stem split showed. Measured back: 140.6 BPM, E minor; -13.3 LUFS, -1.0 dBFS peak.
- Picture rebuilt on the reference's exact frames (891 frames, 24 fps, 37.125 s): sentence-case Inter Display with violet-to-white word settle, accelerating stagger, dot-matrix wipe, continuous pull-back with accelerating exits, the real homepage pill row with whip-zoom and rim streak, "Introducing example film" with an 8th-note echo and breathing bands, the real example film page rising with tilt-shift and a rack-focus dive, macro card with a reward ticker and a self-pressing button, glare-and-frost flip, macro slider (1 to 10%), toggle, accordion, snap re-frames, button-to-dots, layered dashboard with sheen, accelerating creator-card carousel, one white frame, URL, typed wordmark. 16 sub-frames per frame with a 180-degree shutter (8 samples; 4 left stepped ghosts on the whip-zoom), then a lens pass (radial edge blur, vignette, bloom, grain, slight fringe).
- Measured against the reference (same tool, same frames): edge/centre sharpness 0.80 vs 0.86 (cut 10: 1.01); camera scale change per frame 0.32% vs 0.44% (cut 10: 0.03%); grain 2.7 vs 2.9.
- Files: `cuts/cut11/` (film.src.html, build_music.py, post.py, rebuild.sh), `storyboard/cut11-shot-map.md`, preview `previews/refer-earn-cut11_reference-replica_16x9_24fps.mp4`. Waiting on the owner's viewing and listening pass.

## 2026-11-09 - Cut 12 reference teardown ("How Every Decimal Matters", BTC)
- Owner supplied brand's own client-approved 100 s, 30 fps explainer (1920x1080, black, lens + ruler, VO + subtitles) and a revised 77 s script. Measured it with ffprobe, 1 fps sheets, 30 fps subtitle-strip diff and STFT band onsets: 10 scenes, VO sentence timings, two whip transitions (5.6 s, 27.6-28.1 s), dot-matrix dissolve at 58.4 s, audio is voice-dominant with no clearly isolable music bed.
- Found 14 gaps against the revised script (flat 2D lens, zoomed 96,2xx scale instead of 110K-60K, YOU not marked, settled list contradicts "YOU #1", garbled title cross-fade at 41 s, tie-break order and 70% wording differ from the script, capacity bar fills to 10,000 under "EVENT NOT FULL", text-only dead holds). Written up with a target timeline in `storyboard/cut12-reference-teardown.md`. Nothing built yet; waiting on the owner for VO source, real forecast UI screenshots, logo confirmation and approval.

## 2026-11-09 - Reference deep pass v2 (no new cut yet)
- Owner rated cut 10 at 6.5-7/10 and asked for a much deeper, frame-by-frame pass before cut 11. Read every one of the reference's 891 frames on labelled 24-frame sheets, pulled full-resolution crops for type and texture, and measured per frame: centre vs edge sharpness, vignette, grain, chroma and camera scale (ORB similarity). Per-hit sound analysis (band rise, centroid, decay, pitch, width), beat grid and log spectrograms. Ran the same tools on cut 10 for a like-for-like table.
- Found 15 major misses (continuous camera pull-back on every hold, sentence-case medium grotesque with bloom and star glint, blue-to-white word settle with accelerating stagger, recede-and-arrive text transitions, real depth of field, macro UI framing with 2-frame snap re-frames, glare-and-frost glass reveals, exploded dashboard layers, an 8th-note ghost echo, LED dot-screen texture, whip-zoom pill row, an accelerating carousel, and the sound's tempo, density and silences).
- Corrected pass 1: the music is 140 BPM half-time (beat 0.427 s), not 92.9; the carousel accelerates (4 to 2 frames per swap); the music chokes 1-6 frames after the white frame rather than hitting before it; the outro is a reverse swell into a sub boom on the URL, not a drone and ping.
- Measured gaps: frozen frames 6% (reference) vs 20% (cut 10); camera scale change per frame 0.44% vs 0.03%; edge/centre sharpness 0.80 vs 1.03; strong hits per second 1.05 vs 2.83; hit brightness 3.4 vs 5.5 kHz; quietest 10% -65 vs -31 dB.
- Owner decisions recorded: follow the script's 15% / 10%; real brand UI may be shown; creator role cards approved; no paid features. Cut 11 waits for the owner's approval of the report.

## 2026-11-08 - Cut 10 "Glass Planes": reverse-engineered a reference film, rebuilt it for brand
- Owner supplied a 37 s, 24 fps launch film from another company as a style reference. Broke it down with ffprobe, per-frame difference (131 of 891 frames held, one white flash frame at 28.17 s), dense frame sheets of every transition, band-split audio onsets and a spectrogram: 12 shots, 0.646 s beat (92.9 BPM), sub-led pulse, one hit one frame before the white flash then 1.1 s of silence, drone, silent logo. Full written breakdown kept locally (study only).
- Read the live uniocean.io CSS tokens (dark `#0f0f0f`, surface `#1a0e2e`, brand gradient `#9028a5 -> #6128d2`, Lato) and the docs' Referral Dashboard page, then rebuilt the reference's grammar in code: blur-in words, dot-matrix dissolve, glass pill that becomes the title, 3D plane with rack focus, odometer, edge-on flip, cursor-driven ticket, split-open text, dashboard parallax, beat-locked carousel, 2-frame white flash.
- Cut 10: 48 s, 60 fps, 120 BPM, Mixkit "Electro Dreams" offset 8.1 s so the first kick lands on the plane rise, 114 Sonniss cues with odometer ticks computed from the picture's own easing curve. Render: 11,520 sub-frames in about 5 min, tmix to 2,880 frames. Files: `cuts/cut10/`, `storyboard/cut10-beat-sheet.md`.
- QA on the final render (48.00 s, 2,880 frames, 60 fps): -15.4 LUFS, -2.5 dBTP; Video Director QA: frame 0, flashes, pops, planned cuts all pass (planned cut error 0.42 frame). Earshot 0.769 -> 0.897 (21 of 23 in range, 0 critical, 2 major) after letting a gong ring over the end card (dead air 3.2 s -> 0), softening ticks 2.5 dB, adding the dive accent. Left open on purpose: onset on 3 visual events (33%), hit density 2.06/s, and several 1-4 s text-only holds that QA flags as frozen (the reference holds the same way; the owner decides).
- Still open: C1 (docs show 10% / 5% example rates, script says 15% / 10%), C9 (permission to show real UI: this cut rebuilds the UI in HTML and labels figures "Illustrative"), music Content ID, the owner's listening pass.

## 2026-11-08 - Take One run (cut 9), Subframe MCP installed
- Owner approved running Take One (code-only, free), dropped Rossark and Skillry, and approved the Subframe Motion MCP. Cut 9 = Take One monochrome launch film (37.15 s, 60 fps, -14.0 LUFS): Earshot launch-grade 23 of 23, Video Director QA 0 fails. Look: black and white worlds that invert on the beat, the brand gradient only on the two rates. Competitor study and Take One's job log in `cuts/take-one/` (Polymarket and Kalshi pages unreachable from this network; not bypassed).

## 2026-11-08 - Tool comparison: principle skills
- Video Director QA run on all seven cuts; its findings (flat frame 0, loudness under -14 LUFS, long holds) plus the Lottie checklist and Emil choreograph rules applied to the Product Launch cut as v2: frozen picture 45.9% -> 2.7%, frame 0 and loudness pass. Earshot launch kit (72 code-made takes) remix: launch-grade 0.923 vs 0.974 for the Sonniss recordings. Details in `docs/TOOL-COMPARISON.md`.

## 2026-11-08 - Tool comparison: production tools
- Built and scored Huashu Art Motion (launch-grade 0.974), Animate riso (launch-grade 0.974, 24 fps, no real UI), Argo (needs work 0.744, demo-recorder; found the docs-vs-script rate conflict). Take One deliberately not run (about 0.4-0.7M tokens, asks before spending). Results table and lessons in `docs/TOOL-COMPARISON.md`.

## 2026-11-08 - Tool comparison: first three cuts
- Director disliked cut 7's background and music and asked to test a list of motion skills and libraries by making one cut of the same script with each. Shared brief, scorecard and a finishing script (`cuts/_tools/finish_cut.py`) so every cut is measured the same way.
- Built and scored: Product Launch Motion (launch-grade 0.973), Huashu Motion (0.923; synthesized-music flag), Explainroo (0.897; narrated, 30 fps). Full table and lessons: `docs/TOOL-COMPARISON.md`.
- New shared renderer `tools/render_seek.mjs` (seek(t) pages, one browser per worker, 4-subframe motion blur, ffmpeg tmix). Shared music edit (Pixabay 562842, 117 BPM). 12 resources still to build (see the comparison page).

## 2026-11-07 - Cut 7 "Under the Surface" (fresh film) and a lean model set
- Owner asked for a completely fresh cut using everything built so far, and for stale models and assets to be removed.
- **Cleanup:** deleted the weights and leftovers that were judged low quality or superseded (HyperFlow, MiniMax H3, Qwen-Image 2.1, LTX, SDXL, T5, ESRGAN, install wheels, third-party node packs): about 105 GB freed on D:. Kept only Wan 2.2 5B (Apache-2.0) and FLUX 3 Klein with their encoders and VAEs.
- **Cut 7:** new concept (a dark-ocean descent), new music (Pixabay #594242 at 172 BPM, edited on bar lines, drop at 11.146 s), new plates (4 FLUX 3 stills, 3 Wan 2.2 i2v clips plus the earlier sea dolly), 85 real Sonniss sound effects, eight unique transitions including a collapse-to-a-point twist before the drop. 32.17 s, 1920x1080, 60 fps, mastered at -15.4 LUFS with a -2.7 dBFS peak. Earshot: launch-grade, 23 of 23 metrics in range.
- **Plate pipeline that worked:** FLUX 3 still -> Wan 2.2 i2v (97 frames, about 8 minutes each) -> `tools/cut7_plate_convert.py` (optional slow-down, motion-compensated interpolation to 60 fps, crop to 16:9). Scripts: `tools/comfy_cut7_plates.sh`, `tools/cut7_plate_convert.py`.
- **Lesson:** a dark film makes frame-difference measures read low; keep long holds moving with linear (ease none) zooms and slow drifts, not ease-out tweens that settle to a stop.

## 2026-11-07 - Cut 6: cut 1 recreated exactly in 16:9 (nothing added)
- Owner asked for an exact recreation of cut 1 for the bigger screen: same content, music and screens, only smoother. Cut 5 (which added things) is kept; cut 6 replaces it as the answer to that request.
- New project `video6/` (cut 1's six scenes re-laid out for 1920x1080, sources in `video6/src/`, built by `build.py`). Same copy, same scene order, same timings and animation beats as cut 1 (43 s, 120 BPM), rendered at 60 fps instead of 30.
- Soundtrack is cut 1's own mix, unchanged (`assets/audio/refer-earn-cut1-mix.wav`, copied from `archive/cut1/`): same music, same 79 sound cues.
- Layout changes only, because 9:16 stacks do not fit 16:9: title on one line, "Earn commissions" on one line, diagrams spread across the width, the link card beside its heading, tiles in a 2x2 grid beside the "Track your results" heading, "Two levels. One link." on one line, end card as one centred block with the two rates side by side.
- No new assets, no generated media, no licence-limited models. Licence log unchanged apart from a pointer.
- Check: 0 errors; one craft warning kept from cut 1's timing ("Track your results" holds 0.96 s in the recap).

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

## 2026-11-07 - Listening verdict, Sonniss, Resolve
- Owner listened to HyperFlow audio: unusable. i2v: smooth motion, mediocre quality.
- Sonniss GDC 2024 bundles 1-6 extracted and indexed (503 WAVs, not in the public repo).
- DaVinci Resolve 21.2 installer downloaded by owner; owner installs it (admin needed).

## 2026-11-07 - MiniMax H3 pruned w6a8 (native ComfyUI) tested
- `minimax_h3_fl2va_pruned_w6a8.safetensors` (16 GB) + 4-step turbo LoRA + MiniMaxH3SigmaShift 12/3, BasicScheduler simple 4 steps, euler, no CFG. Same plate and prompt as HyperFlow: 960x544, 124 frames, 574 s (HyperFlow 455 s). Mean frame difference 17.8 (HyperFlow 13.5). Palette held, more dramatic (glowing sun appears) but heavy smear/ghosting around frame 90. Verdict: more motion, less clean than HyperFlow. Licence-limited: test only. Audio not evaluated (generated audio already judged unusable).
- Scripts: `tools/comfy_h3_w6a8_test.py`, `comfy_h3_w6a8_run.sh`.
