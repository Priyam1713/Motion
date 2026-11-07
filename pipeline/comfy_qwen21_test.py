"""Qwen-Image 2.1 (int8 convrot) text-to-image via ComfyUI API. Research-only licence: test/internal only.
  python comfy_qwen21_test.py "prompt" prefix [w h steps cfg]"""
import json, sys, time, urllib.request
HOST="http://127.0.0.1:8188"
p,prefix=sys.argv[1],sys.argv[2]
W=int(sys.argv[3]) if len(sys.argv)>3 else 1664
H=int(sys.argv[4]) if len(sys.argv)>4 else 928
S=int(sys.argv[5]) if len(sys.argv)>5 else 25
C=float(sys.argv[6]) if len(sys.argv)>6 else 4.0
wf={
 "1":{"class_type":"UNETLoader","inputs":{"unet_name":"qwen_image_2.1_int8_convrot.safetensors","weight_dtype":"default"}},
 "2":{"class_type":"CLIPLoader","inputs":{"clip_name":"qwen3vl_8b_w4a8.safetensors","type":"qwen_image","device":"default"}},
 "3":{"class_type":"VAELoader","inputs":{"vae_name":"qwen_image_2.1_vae_bf16.safetensors"}},
 "4":{"class_type":"ModelSamplingAuraFlow","inputs":{"model":["1",0],"shift":3.1}},
 "5":{"class_type":"CLIPTextEncode","inputs":{"text":p,"clip":["2",0]}},
 "6":{"class_type":"CLIPTextEncode","inputs":{"text":"","clip":["2",0]}},
 "7":{"class_type":"EmptySD3LatentImage","inputs":{"width":W,"height":H,"batch_size":1}},
 "8":{"class_type":"KSampler","inputs":{"model":["4",0],"positive":["5",0],"negative":["6",0],"latent_image":["7",0],"seed":5,"steps":S,"cfg":C,"sampler_name":"euler","scheduler":"simple","denoise":1.0}},
 "9":{"class_type":"VAEDecode","inputs":{"samples":["8",0],"vae":["3",0]}},
 "10":{"class_type":"SaveImage","inputs":{"images":["9",0],"filename_prefix":prefix}},
}
req=urllib.request.Request(HOST+"/prompt",json.dumps({"prompt":wf}).encode(),{"Content-Type":"application/json"})
try: pid=json.load(urllib.request.urlopen(req))["prompt_id"]
except urllib.error.HTTPError as e: print(e.read().decode()[:3000]); sys.exit(1)
t0=time.time()
while True:
    h=json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
    if pid in h:
        st=h[pid]["status"]; print("status",st.get("status_str"),"in %.1fs"%(time.time()-t0))
        if st.get("status_str")!="success": print(json.dumps(st)[:3000])
        print(h[pid]["outputs"]); break
    time.sleep(2)
