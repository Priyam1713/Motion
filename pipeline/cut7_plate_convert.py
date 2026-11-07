"""Convert a raw Wan clip to a 1920x1080 60 fps scene plate, optionally slowed.
  python cut7_plate_convert.py raw.mp4 out.mp4 [slow=1.0]
Slowing is done by frame retiming (setpts) and motion-compensated interpolation to 60 fps."""
import subprocess, sys
src, dst = sys.argv[1], sys.argv[2]
slow = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
vf = f"setpts=PTS*{slow},minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-an", "-vf", vf, "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-r", "60", dst], check=True)
print("ok", dst)
