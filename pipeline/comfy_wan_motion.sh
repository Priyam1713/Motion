#!/usr/bin/env bash
cd ~/ComfyUI
cp /mnt/d/client/Motion/previews/comfy/flux3-test-01.png input/flux3-test-01.png
. .venv/bin/activate
curl -s http://127.0.0.1:8188/system_stats > /dev/null || { nohup python main.py --listen 127.0.0.1 --port 8188 > ~/comfy_run.log 2>&1 & for i in $(seq 1 60); do curl -s http://127.0.0.1:8188/system_stats > /dev/null && break; sleep 3; done; }
T=/mnt/d/client/Motion/tools/comfy_wan_test.py
python $T i2v "the camera dollies forward fast and low over the glossy violet liquid waves, big swells roll toward the lens and crest, spray and glowing droplets fly past, strong dynamic motion, cinematic" wan_i2v_dolly 97 1280 704 flux3-test-01.png
python $T t2v "fast aggressive camera sweep around huge breaking waves of violet glass, shards of light and water bursting toward the camera, high energy, rapid motion, cinematic lighting, dark background" wan_t2v_burst 97 1280 704
