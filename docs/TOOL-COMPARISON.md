# Tool comparison: one script, many motion tools

**Why this page exists.** We took a list of agent skills and libraries for motion video and used each one to make a cut of the *same* script (a 30-60 s promo for a referral programme: title, 15% direct, 10% second level, three steps, a partner invitation, an end card), paired with the same assets (real product captures, real sound effects, one shared music track unless the tool composes its own). The goal is to learn which ones are actually worth keeping. Brief and scorecard: `brief/shared-brief-v2.md` (private project); results below.

**Scorecard (same for every cut).** Format (1920x1080, 60 fps), loudness and true peak, frozen-picture share, an Earshot critique against its bundled launch films, setup effort, render time, and a human verdict (watch and listen; Claude can only measure).

## Results so far (3 of 15 built)

| Tool | What it is | Setup | Render | Format | Loudness / peak | Earshot | Verdict so far |
|---|---|---|---|---|---|---|---|
| **Product Launch Motion** (AbubakrChan) | A skill that makes a launch film from plain HTML: one shape that never cuts, closed-form springs, a cursor that drives every change, music-first timing, 4-subframe motion blur | Clone the repo, read two reference files; no install (we used `puppeteer-core` + system Chrome + ffmpeg); about 60 min to write the film | 2.5 min for 7,848 subframes at 3 workers, 27 s ffmpeg assemble | 1920x1080 60 fps | -15.3 LUFS / -3.0 dBFS | **launch-grade 0.973**, 0 issues | **Makes films.** Best look and the best score. The method is the value: the one-shape idea gave the film a continuous, premium feel. |
| **Huashu Motion** (alchaincyf) | A skill plus a zero-dependency Node CLI (`om`): templates, a live studio with point-at-the-frame comments, a composer that writes and renders an original score from ABC notation, built-in sound effects, `check` and `qa` | Node 24 + Chrome + ffmpeg only; `om samples build` fetches 44 MB of CC0/CC-BY instruments (needs a `bsdtar` on PATH; set `OM_SAMPLES` and `OM_HOME` to keep it off C:); about 35 min | 1m43 with motion blur | 1920x1080 60 fps (put `data-fps="60"` on the composition root, not on `<html>`) | -14.2 LUFS / -0.8 dBFS after our limiter | needs work 0.923: 22 of 23 metrics in range; the one critical issue is "realness": Earshot judges the composed music as **code-synthesized** | **Improves films.** Excellent tooling (check, still, sound, qa, studio) and a real composer, but its default music and effects sound synthesized to Earshot, and the layout it produced held still for long stretches (57% frozen). Use its checks and composer for drafts; mix real recordings for delivery. |
| **Explainroo** (vincentsch) | Narrated explainers: `script.md` + `scenes.js` -> local Kokoro voice, Whisper word timing, a camera that follows the narration, captions, chapters | `npm install` (67 packages) + 386 MB of local models (put `HF_HOME` on D: and move `~/.cache/explainroo` to D: with a junction); about 70 min including the model downloads | 52 s | 1920x1080 at **30 fps** | -14.1 LUFS / -1.1 dBFS | close 0.897: 20 of 23; one major issue | **Makes narrated films.** Fast and well checked (`check` found real layout and cue mistakes), good for explainers; the voice and the generic "clean" theme read as AI-made. Not the tool for a music-led launch film. |

## What we learned (reusable)

- **Setup gotchas.** Huashu's sample build needs `bsdtar` (copy `C:\Windows\System32\tar.exe` to a folder on PATH as `bsdtar.exe`); Explainroo's model fetch needs retries on flaky networks; both default to caches on C:, so redirect them to D:. A headless-Chrome renderer must give **each worker its own browser**: several tabs in one browser stall (background tabs don't paint).
- **Measuring a film.** The same Earshot critique works for every cut, but its "realness" check punishes code-synthesized sound. Real recordings (our Sonniss effects, a licensed track) score better than any tool's built-in synth.
- **Frozen-picture share** (`ffmpeg freezedetect`) flags bright, calm layouts as "frozen" even when type animates; judge it by eye too.
- **Loudness.** The AAC encode overshoots; mix to about -15 LUFS with a limiter at -1.5 dBFS, then re-measure the master.
- **Invented UI.** Skills that "rebuild" a product screen in code invent labels. Use real captures only, and keep claims and qualifiers on screen.

## Not yet built (12), with what each needs

| Tool | Kind | Plan / blocker |
|---|---|---|
| Huashu Art Motion | Artistic styles and explainer grammars (Chinese-first docs) | Feasible; pick one of its 36 styles for the same script |
| Animate (cth9191) | Procedural single-canvas films, riso/paper/ink styles, approval gates | Feasible; needs Playwright + Chromium; draws everything in code (no real UI unless assets are opted in) |
| Argo | Playwright walkthrough of a real site + local TTS voiceover | Feasible with Kokoro; needs permission to record the live product (C9) |
| Take One | Multi-stage creative pipeline, code-only free path | Tested on macOS only; heavy; try the code-only path |
| Video Director | Planning, timeline validation, automated checks | Use its checks on the cuts above |
| Emil Kowalski skills, LottieFiles motion-design skill | Motion craft principles (easing, timing, choreography) | Apply as a review checklist and measure what changes |
| Earshot | Audio analysis and code-made sound effects | Already used for every critique; next: re-mix one cut with its `launch` kit and compare |
| Reanimate | Recreate a web animation by frame comparison | Needs a reference animation to copy; Bun |
| Rossark Motion | Animating drawn SVG characters for React Native / SwiftUI | Mostly not for video; test on the referral avatars only |
| Subframe Motion | 309 open-source React animations and WebGL shaders, delivered over an MCP server | Needs your OK to install the MCP; examples can inspire backdrops without it |
| Skillry LaunchMotion | 208 editable launch scenes for Claude Code | Paid library (Pro); no spend without your OK |
