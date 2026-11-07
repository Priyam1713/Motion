"""MiniMax H3 (pruned w6a8 + 4-step turbo LoRA) image-to-video through the ComfyUI API. Run inside WSL.
  python comfy_h3_nvfp4_test.py "prompt" out_prefix first_frame.png [width height length steps]
Licence-limited (MiniMax H3 Community License): test/internal only."""
import json, sys, time, urllib.request
HOST = "http://127.0.0.1:8188"
prompt_text, prefix, img = sys.argv[1], sys.argv[2], sys.argv[3]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 960
H = int(sys.argv[5]) if len(sys.argv) > 5 else 544
L = int(sys.argv[6]) if len(sys.argv) > 6 else 124
S = int(sys.argv[7]) if len(sys.argv) > 7 else 4
wf = {
 "1a": {"class_type": "UNETLoader", "inputs": {"unet_name": "minimax_h3_fl2va_pruned_w6a8.safetensors", "weight_dtype": "default"}},
 "1b": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1a", 0], "lora_name": "minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors", "strength_model": 1.0}},
 "1": {"class_type": "MiniMaxH3SigmaShift", "inputs": {"model": ["1b", 0], "shift_video": 12.0, "shift_audio": 3.0}},
 "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "type": "minimax", "device": "default"}},
 "3": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_video_vae_fp16.safetensors"}},
 "4": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_audio_vae_fp32.safetensors"}},
 "5": {"class_type": "MiniMaxH3ImageToVideo", "inputs": {"clip": ["2", 0], "vae": ["3", 0], "prompt": prompt_text, "width": W, "height": H, "length": L, "first_frame": ["20", 0]}},
 "6": {"class_type": "BasicScheduler", "inputs": {"model": ["1", 0], "scheduler": "simple", "steps": S, "denoise": 1.0}},
 "7": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
 "8": {"class_type": "RandomNoise", "inputs": {"noise_seed": 42}},
 "9": {"class_type": "BasicGuider", "inputs": {"model": ["1", 0], "conditioning": ["5", 0]}},
 "10": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["8", 0], "guider": ["9", 0], "sampler": ["7", 0], "sigmas": ["6", 0], "latent_image": ["5", 1]}},
 "11": {"class_type": "VAEDecode", "inputs": {"samples": ["10", 0], "vae": ["3", 0]}},
 "12": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["10", 0], "vae": ["4", 0]}},
 "13": {"class_type": "CreateVideo", "inputs": {"images": ["11", 0], "audio": ["12", 0], "fps": 24}},
 "14": {"class_type": "SaveVideo", "inputs": {"video": ["13", 0], "filename_prefix": prefix, "format": "mp4"}},
 "20": {"class_type": "LoadImage", "inputs": {"image": img}},
}
req = urllib.request.Request(HOST + "/prompt", json.dumps({"prompt": wf}).encode(), {"Content-Type": "application/json"})
try:
    pid = json.load(urllib.request.urlopen(req))["prompt_id"]
except urllib.error.HTTPError as e:
    print(e.read().decode()[:3000]); sys.exit(1)
t0 = time.time()
while True:
    h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        print("status", st.get("status_str"), "in %.1fs" % (time.time() - t0))
        if st.get("status_str") != "success": print(json.dumps(st)[:3000])
        print(h[pid]["outputs"]); break
    time.sleep(3)
