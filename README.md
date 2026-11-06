# Motion: a production-grade motion-video kit for Claude

A living directory of the tools, scripts, rules and lessons we use to make studio-quality motion films with Claude Code.
Written so that a complete beginner can replicate the setup and so that Claude can pick up where the last pass stopped.

**Status:** see [docs/CHANGELOG.md](docs/CHANGELOG.md). This repo is updated after every production pass (see [docs/MAINTENANCE-RULE.md](docs/MAINTENANCE-RULE.md)).

## What is in here

| File | What it answers |
|---|---|
| [docs/SETUP.md](docs/SETUP.md) | How do I replicate this machine setup (Windows + WSL2 + GPU)? |
| [docs/TOOLS.md](docs/TOOLS.md) | Which tool does which job, its licence, and whether it worked for us |
| [docs/WHAT-WORKS.md](docs/WHAT-WORKS.md) | Techniques that gave a visible quality jump |
| [docs/DOS-AND-DONTS.md](docs/DOS-AND-DONTS.md) | Rules learned the hard way (including client feedback) |
| [docs/GOTCHAS.md](docs/GOTCHAS.md) | Renderer, shell and Windows traps, with fixes |
| [docs/RESOURCES.md](docs/RESOURCES.md) | Free music, SFX, images, 3D, icons, fonts: where to get them and what to check |
| [docs/beginner-guide.md](docs/beginner-guide.md) | Glossary and how to prompt, from a first-time user's view |
| [docs/TODO.md](docs/TODO.md) | What is next, what is blocked, what needs a human |
| [pipeline/](pipeline/) | Reusable scripts: sound mixer, music editor, Blender logo sting, ComfyUI installer |

## The 30-second version

1. Video is built as **HTML + GSAP** and rendered to MP4 by **HyperFrames** (frame-exact, 60 fps). Remotion (React) is installed as a second engine.
2. Sound is designed, not dropped in: music edited on bar lines, then real sound effects placed on the exact animation frames and measured against the music so they are audible.
3. 3D comes from **Blender** (GPU, transparent output), images from the real product site, generative assets from **ComfyUI**.
4. Every cut is archived, every asset licence is logged, and a human approves each gate.

## Not in this repo (on purpose)

Client documents, client brand files, screenshots of a client's product, third-party reference videos, downloaded music and SFX files, and renders. They are either confidential or not ours to redistribute. `scripts/` and `docs/RESOURCES.md` say where to fetch the free ones.
