"""FLUX 3 Image Klein (nvfp4) text-to-image through the ComfyUI API. Run inside WSL.
  python comfy_flux3_test.py "prompt" out_prefix [width height steps cfg]"""
import json, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
prompt_text = sys.argv[1]; prefix = sys.argv[2]
W = int(sys.argv[3]) if len(sys.argv) > 3 else 1920
H = int(sys.argv[4]) if len(sys.argv) > 4 else 1088
STEPS = int(sys.argv[5]) if len(sys.argv) > 5 else 4
CFG = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
wf = {
 "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "flux3-image-klein-nvfp4.safetensors", "weight_dtype": "default"}},
 "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_4b_int8_convrot.safetensors", "type": "flux3", "device": "default"}},
 "3": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
 "4": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["2", 0]}},
 "5": {"class_type": "CLIPTextEncode", "inputs": {"text": "", "clip": ["2", 0]}},
 "6": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": W, "height": H, "batch_size": 1}},
 "7": {"class_type": "CFGGuider", "inputs": {"model": ["1", 0], "positive": ["4", 0], "negative": ["5", 0], "cfg": CFG}},
 "8": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
 "9": {"class_type": "Flux2Scheduler", "inputs": {"steps": STEPS, "width": W, "height": H}},
 "10": {"class_type": "RandomNoise", "inputs": {"noise_seed": 5}},
 "11": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["10", 0], "guider": ["7", 0], "sampler": ["8", 0], "sigmas": ["9", 0], "latent_image": ["6", 0]}},
 "12": {"class_type": "VAEDecode", "inputs": {"samples": ["11", 0], "vae": ["3", 0]}},
 "13": {"class_type": "SaveImage", "inputs": {"images": ["12", 0], "filename_prefix": prefix}},
}
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
    time.sleep(2)
