"""brand mark as a 3D object: extruded, glossy violet, lit by a CC0 studio HDRI, with a slow orbit.

Run (from <project>\video\blender):
  ..\..\tools\blender-4.5.15-windows-x64\blender.exe --background --python logo_sting.py -- --frames 120 --samples 48 --out ..\..\previews\3d\logo-sting\f_
  add  --still 60  to render one test frame.
"""
import bpy, sys, math, os
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(name, default):
    return argv[argv.index(name) + 1] if name in argv else default
FRAMES = int(arg("--frames", "120")); SAMPLES = int(arg("--samples", "48")); OUT = arg("--out", r"<project>\previews\3d\logo-sting\f_")
STILL = int(arg("--still", "0")); RES = int(arg("--res", "100"))
HERE = os.path.dirname(os.path.abspath(__file__))
HDRI = os.path.normpath(os.path.join(HERE, "..", "..", "assets", "3d", "hdri", arg("--hdri", "brown_photostudio_02_2k.hdr")))

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.samples = SAMPLES
sc.cycles.use_denoising = True
sc.cycles.denoiser = "OPENIMAGEDENOISE"
try:
    prefs = bpy.context.preferences.addons["cycles"].preferences
    for kind in ("OPTIX", "CUDA"):
        try:
            prefs.compute_device_type = kind; prefs.get_devices()
            if any(d.type == kind for d in prefs.devices):
                for d in prefs.devices: d.use = d.type == kind
                sc.cycles.device = "GPU"; print("GPU:", kind, [d.name for d in prefs.devices if d.use]); break
        except Exception as e:
            print("device", kind, e)
except Exception as e:
    print("no GPU", e)
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1920, 1080, RES
sc.render.fps = 60
sc.frame_start, sc.frame_end = 1, FRAMES
sc.render.film_transparent = True
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGBA"; sc.render.image_settings.color_depth = "8"
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Punchy"

# world from the HDRI
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
nt = w.node_tree; nt.nodes.clear()
env = nt.nodes.new("ShaderNodeTexEnvironment"); env.image = bpy.data.images.load(HDRI)
bg = nt.nodes.new("ShaderNodeBackground"); bg.inputs["Strength"].default_value = 0.7
out = nt.nodes.new("ShaderNodeOutputWorld")
nt.links.new(env.outputs["Color"], bg.inputs["Color"]); nt.links.new(bg.outputs["Background"], out.inputs["Surface"])

# the mark
bpy.ops.import_curve.svg(filepath=os.path.join(HERE, "brand-mark.svg"))
curves = [o for o in bpy.context.scene.objects if o.type == "CURVE"]
for o in curves: o.select_set(True)
bpy.context.view_layer.objects.active = curves[0]
bpy.ops.object.join() if len(curves) > 1 else None
mark = bpy.context.view_layer.objects.active
mark.name = "mark"
cd = mark.data
L = max(mark.dimensions.x, mark.dimensions.y)   # the SVG import is tiny (about 0.04 units), so size the extrusion from it
cd.dimensions = "2D"; cd.fill_mode = "BOTH"; cd.extrude = L * 0.045; cd.bevel_depth = L * 0.016; cd.bevel_resolution = 6; cd.resolution_u = 24
bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
mark.location = (0, 0, 0)
dim = mark.dimensions; s = 6.0 / max(dim.x, dim.y); mark.scale = (s, s, s)

mat = bpy.data.materials.new("violet"); mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.20, 0.02, 0.85, 1)
bsdf.inputs["Metallic"].default_value = 0.92; bsdf.inputs["Roughness"].default_value = 0.11
for k, v in (("Coat Weight", 0.6), ("Coat Roughness", 0.05), ("Specular IOR Level", 0.6)):
    if k in bsdf.inputs: bsdf.inputs[k].default_value = v
mark.data.materials.append(mat)

# rim and fill lights
def area(name, loc, energy, size, color):
    l = bpy.data.lights.new(name, "AREA"); l.energy, l.size, l.color = energy, size, color
    o = bpy.data.objects.new(name, l); sc.collection.objects.link(o); o.location = loc
    d = Vector((0, 0, 0)) - Vector(loc); o.rotation_euler = d.to_track_quat("-Z", "Y").to_euler(); return o
area("rim", (-5, 4, 4), 900, 4, (0.8, 0.6, 1.0)); area("fill", (5, -3, 2), 350, 5, (1, 1, 1))

# camera with a gentle dolly and the mark's orbit
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.lens = 70; cam.data.dof.use_dof = True; cam.data.dof.focus_object = mark; cam.data.dof.aperture_fstop = 5.6
def look(o, target=(0, 0, 0)):
    o.rotation_euler = (Vector(target) - o.location).to_track_quat("-Z", "Y").to_euler()
for f, z in ((1, -22), (FRAMES, -17)):
    cam.location = (0, z, 1.2); look(cam); cam.keyframe_insert("location", frame=f); cam.keyframe_insert("rotation_euler", frame=f)
mark.rotation_euler = (math.radians(90), 0, math.radians(-38)); mark.keyframe_insert("rotation_euler", frame=1)
mark.rotation_euler = (math.radians(90), 0, math.radians(16)); mark.keyframe_insert("rotation_euler", frame=FRAMES)
for ob in (mark, cam):
    for fc in ob.animation_data.action.fcurves:
        for kp in fc.keyframe_points: kp.interpolation = "BEZIER"; kp.handle_left_type = kp.handle_right_type = "AUTO_CLAMPED"

if STILL:
    sc.frame_set(STILL); sc.render.filepath = OUT + "still.png"; bpy.ops.render.render(write_still=True)
else:
    sc.render.filepath = OUT; bpy.ops.render.render(animation=True)
print("done")
