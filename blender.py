import bpy, bmesh
from core import *

# run this module in Blender by doing the following in the built-in Python console:
"""
import sys
sys.path.append("/ABSOLUTE_PATH_TO_REPOSITORY/WaveSim/")
from blender import run
run() # (optionally with arguments)
"""

"""
import sys
sys.path.append("/Users/chladeklu/Documents/GitHub/waveSim/")
from blender import run
run() # (optionally with arguments)
"""

DEFAULT_WAVES = [Wave((-0.1,0),1),Wave((0.1,0),1)]

def run(waves=DEFAULT_WAVES,size=2,resolution=100,frames=120):
    point_array = intensity_array(waves,(resolution,resolution),0.1,resolution / size)
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.mesh.primitive_plane_add(size)
    bpy.ops.object.mode_set(mode='EDIT')
    if resolution > 102:
        resolution = 102
    bpy.ops.mesh.subdivide(number_cuts=resolution - 2)
    bpy.ops.object.mode_set(mode='OBJECT')
    me = bpy.context.active_object.data
    bm = bmesh.new()
    bm_out = bmesh.new()
    bm.from_mesh(me)
    vert_counter = 0
    vlist = bm.verts
    vlist = sorted(vlist,key=lambda v: (v.co.x, v.co.y))
    for vert in vlist:
        x,y=int(vert_counter // resolution) , int(vert_counter % resolution)
        vc = vert.co
        vc[2] = (x+y)/1000#point_array[x][y]
        vert_counter += 1
        bmesh.ops.create_vert(bm_out,co=vc)
    bm_out.to_mesh(me)
    bm.free()
    bm_out.free()
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 3
    bpy.context.object.modifiers["Subdivision"].render_levels = 4
    me = bpy.context.object.data

