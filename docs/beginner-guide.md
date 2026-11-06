# Motion video with Claude: a beginner's guide (6 Nov 2026)

Written for the example project (a 34 s referral-programme promo). All timestamps refer to **cut 4** (`previews/refer-earn-cut4_16x9_60fps.mp4`), so you can scrub to each example.

## 1. What we installed and used, and what worked

**Production tools**

| Tool | What it does | Licence | Verdict |
|---|---|---|---|
| Claude Code (desktop) | Me: plans, writes the film as code, runs the tools | n/a | Core |
| HyperFrames 0.9.15 (Claude plugin) | Turns an HTML page with animation into an MP4 (headless Chrome + FFmpeg). Also lint/check, snapshots | Apache-2.0 | **Worked.** Everything is editable text, renders are repeatable |
| GSAP 3.15 | The animation engine inside the page (moves, fades, scales on a timeline) | GSAP free licence | **Worked.** Precise timing on the beat |
| FFmpeg 9.0.1 | Decodes/encodes audio and video, measures loudness | GPL tool | Worked. Needed on PATH for check/render |
| Earshot (MIT) | Sound critic: compares our audio with 7 professional films | MIT | Worked, but blocked at the end by a Windows security policy (not bypassed) |
| Python + numpy/scipy/pyloudnorm | Our mixer (`mix.py`): places effects, ducks music, sets loudness | open source | **Worked.** The big cut 4 upgrade lives here |
| puppeteer-core + Chrome headless shell | Took screenshots of the product site and the docs | open source | **Worked.** Gave us real imagery |
| Geist + Geist Mono | Typefaces | SIL OFL | Worked, matches the references |

**Assets**

| Asset | Source | Used in | Verdict |
|---|---|---|---|
| Music: Pixabay #589018, 180 BPM drum and bass | Pixabay Content License | Cut 4 | **Big upgrade** (fast, full-time). Flag: Content ID registered |
| Earlier music: Mixkit #136 (cut 2), Pixabay "So Easy" 160 BPM (cut 3) | Mixkit / Pixabay | Archived cuts | Replaced: felt slow |
| About 124 sound effects (Mixkit) | Mixkit SFX licence | Cuts 2–4 | Good. In cut 4 we placed them louder and ducked the music |
| Real captures of the product site and the product docs | Client's own site | Cut 4 scenes 3, 6, 8 | **Biggest visual upgrade.** Needs client permission (C9) |
| HyperFrames registry (about 450 ready-made blocks) | Plugin | Browsed; one block tested, not used | We hand-built instead, because the registry's shader demos use static textures |
| Reference films (3 in Downloads + the brand pro film) | You | Studied frame by frame | Set the quality bar |

**What made cut 4 better than cut 3** (in order of impact): real product imagery; unique transition per scene; fast music; audible and ducked sound design; the freeze-and-shatter twist; continuous camera drift so almost nothing sits still (5.9% frozen frames).

**What didn't work:** sliding or reused transitions (cut 2/3); effects 13–20 dB under the music (cut 3); slow half-time music; the renderer silently lowering the soundtrack when the encoded peak was too high (fixed with more headroom).

## 2. Glossary, with timestamps from cut 4

**Timing**
- **BPM** (beats per minute): the music's speed. Cut 4 is **180 BPM**, so one **beat = 0.333 s**.
- **Bar**: 4 beats. Here **1.333 s**. Scenes change on bar lines: 2.67, 5.33, 8.0, 10.67, 16.0, 18.67, 21.33, 24.0, 26.67, 32.0.
- **Downbeat**: beat 1 of a bar, where the heaviest hit lands.
- **Drop**: the moment the music goes full energy. Cut 4: **16.0 s**.
- **Build**: the rising section before the drop (5.33–14.67 s).
- **Breakdown / dip**: the music thins out. Here 14.67–16.0 s.
- **Stop-down**: the sound deliberately cuts out for a beat before a hit. Cut 4: **14.67–16.0 s** (tape stops, heartbeat, then the drop).
- **Hard stop**: music ends dead on a beat, no fade. Cut 4: **32.0 s** (the final hit).
- **Ring-out**: the tail after the last hit (32–34 s).
- **Sync / on the beat**: a visual change lands within about 70 ms of a sound.
- **Frame, fps**: one still image; frames per second. Cut 4 is **60 fps** = 2040 frames, so motion is smoother than 24/30 fps.
- **Timecode style we use**: seconds, e.g. "16.0" or "14.67–16.0".

**Motion and camera**
- **Transition**: how one scene becomes the next. Cut 4 has nine, e.g. **T2 text mask (4.67–5.33 s)**: the "&" grows and the product shows through it.
- **Match cut**: a shape or object stays while the scene changes around it (the number stays while the world flips).
- **Punch-in / push-in**: the camera moves closer. **Pull-out**: it moves away.
- **Dive / zoom through**: the camera flies into an object until it fills the frame (**T1 portal, 2.0–2.67 s**, through the logo's loop).
- **Easing**: how a move accelerates. *ease-out* = fast then settles (landings); *ease-in* = slow then fast (dives); *in-out* = both.
- **Stagger**: items start one after another (the slot-roll letters at 2.67 s, each 0.045 s apart).
- **Parallax**: layers move at different speeds, which gives depth.
- **Motion blur**: smear on fast movers so motion looks natural.
- **Hold**: how long something stays on screen so it can be read. A "dead stretch" is a hold with nothing moving.
- **Kinetic typography**: text that moves (the words blur in one per beat at 3.67 s; the **weight sweep** at 25.33 s where "Let's connect." goes hairline and back).
- **Slot roll**: letters spin like a slot machine before landing (2.67–3.4 s).
- **Counter**: a number counting up (a figure counting up on screen).
- **3D flip / perspective**: a card rotating in depth (**T3, 7.4–8.0 s**).
- **Mask / clip-path**: a shape that decides what is visible. Used for the ampersand (T2), shatter shards (T5, 16.0 s), blinds (T8, 23.5 s), barn doors (T9, 26.17 s).
- **Displacement / ripple**: pixels pushed by a noise pattern, like water (**T4, 10.33–11.0 s**).
- **Halftone**: a dot pattern whose dot size changes (**T6, 18.1–18.67 s**).
- **Chromatic aberration / RGB split**: red and blue channels offset (the freeze at 14.67 s).
- **Shatter**: the frame breaks into shards (T5 at 16.0 s).

**Sound**
- **SFX** (sound effect): any added sound. **UI sound**: clicks, pops, ticks. **Impact / hit**: a short heavy thump on a beat. **Sub**: very low bass. **Riser**: a rising sound into a hit (15.3–16.0 s). **Whoosh**: a sweep sound; we avoid it because it reads cheap.
- **Foley**: real-world recorded sounds (shutter at 5.33 s, glass at 16.0 s, tape stop at 14.67 s).
- **Ducking**: music dips a few dB under a sound so it can be heard. Cut 4 ducks about 5 dB at 16.0 s.
- **Mix levels, dB**: loudness steps; 6 dB is clearly louder. We place effects 1–10 dB under the music's loud level.
- **LUFS**: average loudness of the whole film. Cut 4 is **−15.4 LUFS** (web films sit about −14 to −16).
- **True peak (dBTP)**: the loudest instant; must stay below about −1 so it doesn't distort.
- **Limiter**: a safety that stops peaks going over.
- **Stem**: one part of the mix on its own (music only, effects only), useful for checking.
- **Sound design**: planning which sounds go where. **Music-led**: the music carries the film, effects are accents.

**Files and tools**
- **Composition**: the HTML file that describes the film (`video/src/film.src.html`).
- **Timeline**: the list of animations and when they start. **Tween**: one animation (a move or fade).
- **Render**: turning the page into an MP4. **CRF 12**: high quality (lower is better, bigger). **H.264 + AAC**: the common video + audio formats.
- **Snapshot**: a still frame at a time, used to check the picture before rendering.
- **Lint / check**: automatic error and layout checks.
- **Master**: the final highest-quality file. **Review copy**: a small version for the web page.
- **Source / reproducible**: all inputs kept so the same film can be rebuilt exactly.
- **Archive**: earlier cuts kept in `archive/`.

## 3. How to prompt me (templates)

1. **Time-stamped notes** (best): "At 14.7 s the freeze lasts too long; cut it to 0.5 s. At 24.0 s make 'Let's' land one beat later (24.33)."
2. **Name the layer**: picture, transition, type, music, effect, mix. "Transition T4 (10.33 s) is too violent: halve the ripple."
3. **Say a direction and a number**: "faster", "louder" become "effects 3 dB louder", "BPM 174 or above", "hold the 10% frame 0.5 s longer".
4. **Give references with a timestamp**: "like firecrawl-cli at 20.3 s, the zoom-out reveal."
5. **Give constraints**: what must not change, what is client-approved, what can't be shown (earnings, guarantees).
6. **Ask for options**: "show two versions of the end card".
7. **For sound, tell me what you hear**: "the click at 8.67 s is harsh", "I can't hear the shutter at 5.33 s". I can only measure sound, not hear it.

## 4. What our setup still needs (and what professionals use)

*Research note: web sources on this are mostly vendor marketing, so treat rankings with caution. Sources: [LottieFiles guide](https://lottiefiles.com/blog/design-guides-and-tips/best-motion-design-tools-ranked-by-use-case.md), [Motion Media](https://www.motionmedia.com/mm-blog/best-motion-graphics-software-2026), [ImagineArt](https://www.imagine.art/blogs/best-tools-for-motion-design), [Contra sound-design listing](https://contra.com/s/RFUUL7ZY-sound-design-for-commercial-and-promo-video), [Artlist sound-design tips](https://artlist.io/blog/tips-that-will-take-your-sound-design-to-the-next-level/).*

**Highest impact for this film**
1. **A real screen recording of the product** (not only screenshots): the referral dashboard, Copy link, share flow. Biggest realism gain. Needs the client (C9, plus a recording account).
2. **Brand pack** (official logo files, colours, fonts) and **logo-animation permission** (C8).
3. **A human ear on the mix.** Professionals finish in a DAW or editor (DaVinci Resolve's free Fairlight page, Reaper, Logic) with EQ, compression and sidechain. I can measure but not hear. You, or a freelance sound designer for a few hours, would close the gap.
4. **Content-ID-clear music**, or a licensed track from a paid library (Artlist, Epidemic Sound, etc.). Paid needs your approval; check each licence for client and broadcast use.
5. **Final-delivery formats**: a ProRes/high-bitrate master, a 9:16 and 1:1 cut, subtitles/captions for sound-off viewing.

**What professionals use (and where it would help us)**
- **After Effects**: the default tool for motion graphics. We replicate its look in code; it is only needed if a motion designer joins and wants editable AE layers.
- **Cinema 4D or Blender (free)**: real 3D (a glassy 3D logo, coins, devices with depth of field and reflections). Biggest "premium" jump after real footage. Blender is free; we could render a 3D logo or product object and import it.
- **Rive or Lottie**: lightweight vector animation (icons, UI micro-interactions) that can be reused on the website.
- **DaVinci Resolve (free) or Premiere**: editing, colour grading and audio finishing.
- **Sound libraries**: Soundly / Artlist / Epidemic / Video Copilot Designer SFX for richer layered sounds; **layering** several sounds per hit (sub + click + air) is the standard trick.
- **Code-based motion** (what we do, with HyperFrames; also Remotion, Motion Canvas): good for data-driven or batch versions.

**Free upgrades we can do inside our setup, no spend**
- Use HyperFrames **registry blocks** (about 450) for light leaks, grain, camera shake, 3D showcase.
- Turn on **render-time motion blur** on fast movers.
- Add **depth**: shadows, glow, depth-of-field blur on background layers, subtle film grain.
- **Layer each hit** (sub + body + air) and add short **reverb tails** to impacts.
- **Freesound (CC0)** and other free libraries for more textures; always log the licence.
- Install **Blender** to make a 3D logo sting; install **DaVinci Resolve** for a final audio pass.
- An A/B **test render at 30 and 60 fps**, and a **mobile-size check** (does 38 px type read on a phone?).

## 5. Working agreement

- You review picture and sound and send timestamped notes; I measure, build and report numbers.
- I ask before spending money or touching system settings. Downloads of free resources are pre-approved.
- Every cut is archived, every asset's licence is logged (`assets/licenses/LICENCE-LOG.md`), and every on-screen line is client-approved before publishing (`brief/onscreen-copy-cut4.md`).

## 6. Setup added on 6 Nov 2026 (after cut 4)

**Ready to use**
- **Blender 4.5 LTS** (`tools/blender-4.5.15-windows-x64/blender.exe`) with the GPU (RTX 5070 Ti, OptiX) working. `video/blender/logo_sting.py` turns the brand mark into a glossy 3D object lit by a studio HDRI and renders a turntable with a transparent background.
  - Test result: 90 frames at 60 fps, about 12 s per 1080p frame, encoded to `previews/3d/logo-sting-alpha.webm` (transparent VP9).
  - Run: `blender.exe --background --python logo_sting.py -- --frames 90 --samples 40 --out <folder>_`. Add `--still 70` for one test frame.
  - Next step if you like it: place it in the film (end card at 32.0 s is the natural spot) as a transparent video layer.
- **Free CC0 lighting** (Poly Haven HDRIs) and **Lucide icons**.
- **23 CC0 sound effects** from Openverse, with an index of sources, ready to audition for the next mix.
- **Audacity** (portable) for inspecting and editing audio; **librosa** and **PySceneDetect** for beat and cut analysis; **VMAF** (inside FFmpeg) for scoring export quality.

**Needs you (a normal browser or an account)**
- **Sonniss GameAudioGDC**: the biggest free pro SFX archive. The host blocks scripts. Download any bundle from https://sonniss.com/gameaudiogdc/ into `assets/audio/sfx/sonniss/` and I will index and use it.
- **Soundly Free**, **A Sound Effect Cloud**, **Freesound**: need an account. Drop downloads into `assets/audio/sfx/` and tell me.
- **DaVinci Resolve (free)** for your final listening pass and colour: install it yourself (needs admin); it is the best place for the human-ear mix.
- **Inkscape, Krita**: only if you want to draw assets yourself.

**Looked at and deliberately not installed (yet)**
- **Remotion**: great, but its free licence depends on company size, and HyperFrames already covers the job. We can trial it in a separate folder if you want a comparison.
- **ComfyUI + generative image/video models, ACE-Step, MMAudio, voice tools**: big downloads with licence checks per model. Worth it only for a specific need (for example AI B-roll). Tell me the shot and I will test one model.
- **Anything with paid generation or non-commercial weights.**

**New working rules**
- You do the listening and the mix review; I measure, build and report.
- Logo animation is allowed.
- Music: avoid paid; prefer Content-ID-clear free tracks (for the film's current track see D14).
