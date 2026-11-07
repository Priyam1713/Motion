"""Headless ComfyUI LTX-Video (2B distilled) text-to-video smoke test. Run inside WSL.
Usage: python comfy_ltx_test.py "prompt" [width height frames]"""
import json, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
prompt_text = sys.argv[1] if len(sys.argv) > 1 else ("slow camera push through deep violet liquid glass waves, glowing particles drifting, "
                                                    "cinematic lighting, smooth motion, dark background, no text")
W = int(sys.argv[2]) if len(sys.argv) > 2 else 768
H = int(sys.argv[3]) if len(sys.argv) > 3 else 448
N = int(sys.argv[4]) if len(sys.argv) > 4 else 97   # frames: 8k+1
FPS = 24
wf = {
 "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "ltxv-2b-0.9.8-distilled.safetensors"}},
 "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "t5xxl_fp8_e4m3fn_scaled.safetensors", "type": "ltxv", "device": "default"}},
 "3": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["2", 0]}},
 "4": {"class_type": "CLIPTextEncode", "inputs": {"text": "worst quality, blurry, jittery, distorted, text, watermark", "clip": ["2", 0]}},
 "5": {"class_type": "LTXVConditioning", "inputs": {"positive": ["3", 0], "negative": ["4", 0], "frame_rate": float(FPS)}},
 "6": {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": W, "height": H, "length": N, "batch_size": 1}},
 "7": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["5", 0], "negative": ["5", 1], "latent_image": ["6", 0],
        "seed": 11, "steps": 8, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
 "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["1", 2]}},
 "9": {"class_type": "CreateVideo", "inputs": {"images": ["8", 0], "fps": float(FPS)}},
 "10": {"class_type": "SaveVideo", "inputs": {"video": ["9", 0], "filename_prefix": "video/ltx_test", "format": "auto", "codec": "auto"}},
}
req = urllib.request.Request(HOST + "/prompt", json.dumps({"prompt": wf}).encode(), {"Content-Type": "application/json"})
try:
    pid = json.load(urllib.request.urlopen(req))["prompt_id"]
except urllib.error.HTTPError as e:
    print(e.read().decode()[:2000]); sys.exit(1)
t0 = time.time()
while True:
    h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        print("status", st.get("status_str"), "in %.1fs" % (time.time() - t0))
        if st.get("status_str") != "success": print(json.dumps(st)[:2500])
        print(h[pid]["outputs"]); break
    time.sleep(3)
