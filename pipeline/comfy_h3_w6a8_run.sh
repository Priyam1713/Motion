#!/usr/bin/env bash
python3 /mnt/d/client/Motion/tools/comfy_h3_w6a8_test.py "The camera dollies fast and low forward over the dark violet sea toward the glowing horizon, waves surge and spray flies past, cinematic, motion-heavy, same violet colour palette" h3w6a8/i2v-test flux3-test-01.png 960 544 124 4
tail -n 25 ~/comfy_run.log | cut -c1-300
