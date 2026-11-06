"""Headless ComfyUI smoke test: SDXL text-to-image through the HTTP API. Run inside WSL with ComfyUI's venv."""
import json, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
prompt_text = sys.argv[1] if len(sys.argv) > 1 else "abstract deep ocean waves made of violet glass, cinematic lighting, dark background, soft glow, no text"
wf = {
 "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "sd_xl_base_1.0.safetensors"}},
 "2": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["1", 1]}},
 "3": {"class_type": "CLIPTextEncode", "inputs": {"text": "text, watermark, logo, blurry, low quality", "clip": ["1", 1]}},
 "4": {"class_type": "EmptyLatentImage", "inputs": {"width": 1344, "height": 768, "batch_size": 1}},
 "5": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["2", 0], "negative": ["3", 0], "latent_image": ["4", 0],
        "seed": 7, "steps": 25, "cfg": 6.5, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1.0}},
 "6": {"class_type": "VAEDecode", "inputs": {"samples": ["5", 0], "vae": ["1", 2]}},
 "7": {"class_type": "SaveImage", "inputs": {"images": ["6", 0], "filename_prefix": "motion_test"}},
}
req = urllib.request.Request(HOST + "/prompt", json.dumps({"prompt": wf}).encode(), {"Content-Type": "application/json"})
pid = json.load(urllib.request.urlopen(req))["prompt_id"]
t0 = time.time()
while True:
    h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
    if pid in h:
        print("done in %.1fs" % (time.time() - t0), h[pid]["outputs"]); break
    time.sleep(2)
