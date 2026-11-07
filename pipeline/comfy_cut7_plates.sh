#!/usr/bin/env bash
# Cut 7 plates: FLUX 3 Klein stills, then Wan 2.2 i2v motion from three of them. Runs inside WSL.
cd ~/ComfyUI; . .venv/bin/activate
curl -s http://127.0.0.1:8188/system_stats > /dev/null || { nohup python main.py --listen 127.0.0.1 --port 8188 --fast-disk --cache-none > ~/comfy_run.log 2>&1 & for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done; }
F=/mnt/d/client/Motion/tools/comfy_flux3_test.py
W=/mnt/d/client/Motion/tools/comfy_wan_test.py
PAL="deep indigo and near-black navy water, brand violet and magenta light, cinematic, ultra detailed, no text"
python $F "A single narrow shaft of violet light descending from the surface into a dark ocean abyss, volumetric rays, drifting particles, $PAL" cut7/s1-abyss
python $F "Looking up from underwater at the rippling surface, glowing violet and magenta caustics, soft rays, drifting particles, $PAL" cut7/s2-surface
python $F "Luminous ribbons of violet and magenta light flowing like ocean currents through pitch-black water, long exposure, streams converging toward the camera, glowing particles, elegant abstract, $PAL" cut7/s3-current
python $F "Dark translucent violet liquid glass swirl, macro, smooth soft gradients, subtle caustics, premium abstract background, near black, $PAL" cut7/s4-glass
for n in s1-abyss s2-surface s3-current s4-glass; do cp output/cut7/${n}_00001_.png input/cut7_$n.png; cp output/cut7/${n}_00001_.png /mnt/d/client/Motion/video7/assets/plates/$n.png; done
python $W i2v "the camera descends smoothly and steadily down the shaft of violet light, particles stream upward past the lens, rays sway, strong clear motion, keep the same violet and navy colour palette, cinematic" cut7/w1-descent 97 1280 704 cut7_s1-abyss.png
python $W i2v "the camera rises toward the rippling surface, caustic light patterns shimmer and sweep across the frame, bubbles drift up, strong clear motion, keep the same violet and navy colour palette, cinematic" cut7/w2-rise 97 1280 704 cut7_s2-surface.png
python $W i2v "the camera glides fast forward along the glowing ribbons of light, streams of violet and magenta current surge past the lens and converge, particles streak by, strong clear motion, keep the same violet and magenta colour palette, cinematic" cut7/w3-flow 97 1280 704 cut7_s3-current.png
for n in w1-descent w2-rise w3-flow; do cp output/cut7/${n}_00001_.mp4 /mnt/d/client/Motion/video7/assets/plates/$n.mp4 2>/dev/null; done
echo PLATES_DONE
