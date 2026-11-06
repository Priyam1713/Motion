# Maintenance rule

**After every production pass, this repo is updated before the pass is called done.** A pass is any session that built, rendered, installed, measured or learned something.

Checklist (Claude does this, then tells the human what changed):

1. `docs/CHANGELOG.md`: add a dated entry (what was done, what was measured, what failed).
2. `docs/WHAT-WORKS.md`: add any technique that clearly helped, with a number or a timestamp.
3. `docs/DOS-AND-DONTS.md`: add every new rule or piece of feedback, in the Do or the Do-not list.
4. `docs/GOTCHAS.md`: add every error that cost time, with its fix.
5. `docs/TOOLS.md` and `docs/RESOURCES.md`: add or re-grade every tool and resource touched (worked / partly / failed / skipped, and why).
6. `docs/TODO.md`: tick what is finished, add what is next, list what needs a human.
7. Run `python tools/sync_repo.py --push` in the working project (it copies only the whitelisted, public-safe files, commits and pushes).
8. Never push client documents, client brand assets, product screenshots, downloaded media, or secrets.

If the push is not possible (offline, auth), say so and leave the staged commit for the next pass.
