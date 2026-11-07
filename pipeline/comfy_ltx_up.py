"""LTX-Video 2B distilled with ESRGAN 4x upscale to 1920x1080. Run inside WSL.
  python comfy_ltx_up.py t2v "prompt" out_prefix
  python comfy_ltx_up.py i2v "prompt" out_prefix input_image.png   (image must be in ~/ComfyUI/input)"""
import json, os, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
mode, prompt_text, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
img = sys.argv[4] if len(sys.argv) > 4 else None
W, H, N, FPS = 768, 448, 97, 24
wf = {
 "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "ltxv-2b-0.9.8-distilled.safetensors"}},
 "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "t5xxl_fp8_e4m3fn_scaled.safetensors", "type": "ltxv", "device": "default"}},
 "3": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["2", 0]}},
 "4": {"class_type": "CLIPTextEncode", "inputs": {"text": "worst quality, blurry, jittery, distorted, text, watermark", "clip": ["2", 0]}},
 "5": {"class_type": "LTXVConditioning", "inputs": {"positive": ["3", 0], "negative": ["4", 0], "frame_rate": float(FPS)}},
}
if mode == "i2v":
    wf["20"] = {"class_type": "LoadImage", "inputs": {"image": img}}
    wf["21"] = {"class_type": "ImageScale", "inputs": {"image": ["20", 0], "upscale_method": "lanczos", "width": W, "height": H, "crop": "center"}}
    wf["6"] = {"class_type": "LTXVImgToVideo", "inputs": {"positive": ["5", 0], "negative": ["5", 1], "vae": ["1", 2], "image": ["21", 0],
               "width": W, "height": H, "length": N, "batch_size": 1, "strength": 1.0}}
    pos, neg, lat = ["6", 0], ["6", 1], ["6", 2]
else:
    wf["6"] = {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": W, "height": H, "length": N, "batch_size": 1}}
    pos, neg, lat = ["5", 0], ["5", 1], ["6", 0]
wf.update({
 "7": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": pos, "negative": neg, "latent_image": lat,
        "seed": 11, "steps": 8, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
 "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["1", 2]}},
 "30": {"class_type": "UpscaleModelLoader", "inputs": {"model_name": "RealESRGAN_x4plus.pth"}},
 "9": {"class_type": "CreateVideo", "inputs": {"images": ["32", 0], "fps": float(FPS)}},
 "10": {"class_type": "SaveVideo", "inputs": {"video": ["9", 0], "filename_prefix": "video/" + prefix, "format": "auto", "codec": "auto"}},
})
# Upscale in 12-frame chunks so the 4x intermediate never exceeds WSL's RAM cap (14 GB).
CH = 12
prev = None
for k, i in enumerate(range(0, N, CH)):
    n = min(CH, N - i)
    a, b, c = str(100 + k * 3), str(101 + k * 3), str(102 + k * 3)
    wf[a] = {"class_type": "ImageFromBatch", "inputs": {"image": ["8", 0], "batch_index": i, "length": n}}
    wf[b] = {"class_type": "ImageUpscaleWithModel", "inputs": {"upscale_model": ["30", 0], "image": [a, 0]}}
    wf[c] = {"class_type": "ImageScale", "inputs": {"image": [b, 0], "upscale_method": "lanczos", "width": 1920, "height": 1080, "crop": "center"}}
    if prev is None:
        prev = c
    else:
        j = str(500 + k)
        wf[j] = {"class_type": "ImageBatch", "inputs": {"image1": [prev, 0], "image2": [c, 0]}}
        prev = j
wf["9"]["inputs"]["images"] = ["8", 0] if os.environ.get("NOUP") else [prev, 0]
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
