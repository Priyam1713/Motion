"""Wan 2.2 TI2V-5B (Apache-2.0) text/image-to-video through the ComfyUI API. Run inside WSL.
  python comfy_wan_test.py t2v "prompt" out_prefix [frames] [width] [height]
  python comfy_wan_test.py i2v "prompt" out_prefix frames width height input_image.png   (image in ~/ComfyUI/input)"""
import json, os, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
mode, prompt_text, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
N = int(sys.argv[4]) if len(sys.argv) > 4 else 49
W = int(sys.argv[5]) if len(sys.argv) > 5 else 1280
H = int(sys.argv[6]) if len(sys.argv) > 6 else 704
img = sys.argv[7] if len(sys.argv) > 7 else None
FPS = 24
neg = "blurry, low quality, jitter, flicker, distorted, text, watermark, static, overexposed"
wf = {
 "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_ti2v_5B_fp16.safetensors", "weight_dtype": "default"}},
 "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
 "3": {"class_type": "VAELoader", "inputs": {"vae_name": "wan2.2_vae.safetensors"}},
 "4": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["2", 0]}},
 "5": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["2", 0]}},
 "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 8.0}},
 "7": {"class_type": "Wan22ImageToVideoLatent", "inputs": {"vae": ["3", 0], "width": W, "height": H, "length": N, "batch_size": 1}},
 "8": {"class_type": "KSampler", "inputs": {"model": ["6", 0], "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["7", 0],
        "seed": 21, "steps": 20, "cfg": 5.0, "sampler_name": "uni_pc", "scheduler": "simple", "denoise": 1.0}},
 "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["3", 0]}},
 "10": {"class_type": "CreateVideo", "inputs": {"images": ["9", 0], "fps": float(FPS)}},
 "11": {"class_type": "SaveVideo", "inputs": {"video": ["10", 0], "filename_prefix": "video/" + prefix, "format": "auto", "codec": "auto"}},
}
if mode == "i2v":
    wf["20"] = {"class_type": "LoadImage", "inputs": {"image": img}}
    wf["21"] = {"class_type": "ImageScale", "inputs": {"image": ["20", 0], "upscale_method": "lanczos", "width": W, "height": H, "crop": "center"}}
    wf["7"]["inputs"]["start_image"] = ["21", 0]
req = urllib.request.Request(HOST + "/prompt", json.dumps({"prompt": wf}).encode(), {"Content-Type": "application/json"})
try:
    pid = json.load(urllib.request.urlopen(req))["prompt_id"]
except urllib.error.HTTPError as e:
    print(e.read().decode()[:2500]); sys.exit(1)
t0 = time.time()
while True:
    h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        print("status", st.get("status_str"), "in %.1fs" % (time.time() - t0))
        if st.get("status_str") != "success": print(json.dumps(st)[:2500])
        print(h[pid]["outputs"]); break
    time.sleep(3)
