# Do and do not

## From the 9 Nov deep pass
- Do keep the camera moving on every hold (slow pull-back on text, push-in on objects) and accelerate into exits.
- Do give UI shots real depth of field and macro framing; one idea per frame.
- Do keep sound sparse, dark and centred around about 1 strong hit per second, with real silences.
- Don't build the next reference cut until the owner approves the breakdown report.

## Do
- **Always use the best available model or tool.** Check what is current (Hugging Face trending, Artificial Analysis, Arena) before choosing; our first picks (SDXL, LTX-Video 2B) were already outclassed. Test candidates before judging them.
- Study references frame by frame (dense contact sheets, motion measurements) before designing.
- Give every transition its own mechanism (portal, mask, flip, ripple, shatter, halftone, grid, blinds, barn doors). Never reuse one.
- Edit music on bar lines at a fast, full-time tempo (about 175-180 BPM drum and bass worked; 160 BPM future bass felt slow).
- Place sound effects 1-10 dB under the music's loud level and duck the music under hits. Measure per cue.
- Use real imagery of the product (headless-browser captures) instead of invented UI. It was the biggest single upgrade.
- Add one creative twist (we froze the picture, then shattered it on the drop).
- Keep camera pushes alive on holds so frames are never frozen for long (measure the frozen-frame share).
- Mix to -15.3 LUFS with a -3 dBTP ceiling so the renderer's loudness guard does not turn the track down.
- Log every asset's licence when it enters the project. Archive old cuts; never delete them.
- Ask the human for what only a human can do: listening to the mix, blocked downloads, sign-offs.
- Keep telemetry off (`HYPERFRAMES_NO_TELEMETRY=1`).

## Do not
- Do not put outputs of licence-limited models (MiniMax H3 / HyperFlow: no display in US/EU/UK/Korea; Qwen-Image 2.1: research-only; gated FLUX 3 until accepted) into a delivered film. Use them for tests and internal looks; deliver with permissively licensed models such as Wan 2.2 (Apache-2.0).
- Do not use cheap whooshes in picture or sound.
- Do not scatter small elements on a static frame, and avoid node-and-line diagrams.
- Do not rely on the same in/out move for several scenes.
- Do not claim Claude heard the mix. Claude measures; the human listens.
- Do not bypass bot protection, CAPTCHAs or paywalls to fetch assets. Ask the human to download in a browser.
- Do not install anything that needs admin rights or changes system settings without asking.
- Do not spend money (music, credits, plans) without approval. Avoid paid music; check Content ID status of free tracks.
- Do not commit client documents, client brand files, product screenshots, third-party videos, downloaded music/SFX or renders to a public repo.
- Do not show percentages, earnings or guarantees in a client film unless the client has approved the exact wording.

- DON'T use the audio that AI video models generate (HyperFlow H3 ocean audio was dull and unusable). DO build the soundtrack from licensed SFX and music.

## From the reference-driven cut (2026-11-08)
- **Do** use a reference's grammar (timing, light, sound structure), never its product, data, logos or assets; replace everything with the client's own.
- **Do** read the client's live CSS tokens and font before choosing colours; use the real brand gradient and the site's own font (Lato).
- **Do** rebuild UI from documented features and label figures "Illustrative" while permission to show the real UI is open.
- **Do** put the impact one frame before a smash cut and let the silence carry it.
- **Do not** let one element sit on screen near-static for more than about a second; add ambient drift (the 26.4-27.5 s dashboard hold was caught by freezedetect).
- **Do not** copy the reference's brand-specific claims; our script's wording ("eligible platform fees", "subject to the programme terms") is kept on screen.

- Do (9 Nov 2026): when the client has already approved a film, measure it before building (subtitle-strip diff gives VO timing without a transcriber) and list where it falls short of the new script; the approved grammar stays, the flaws get fixed.

- Do (9 Nov 2026): rank/price logic must be a real computation (one price path -> ranks, rows, pins, sound cues); a hand-keyed rank list contradicts the pins. Check the script's rank sequence is feasible before drawing: the user pin can only reach #4 or #5 if it is an extreme pin.
- Do not: let two scenes cross-dissolve with readable text (double headers at 34.7 s in the first render); finish the exit before the next scene's text enters.

- Do (9 Nov 2026, owner feedback): crypto/fintech explainers want catchy bling, token, arcade-style SFX (bells, coin pings, pitched blips) in the music's key, plus a quiet upbeat bed; realistic foley (slides, slams, thumps) reads as whooshes and slams and was rejected. Keep SFX synthesized and pentatonic; weight only as a soft thump under a bell.
