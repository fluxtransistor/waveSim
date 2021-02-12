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

DEFAULT_WAVES = [Wave((-0.5,0),0.5),Wave((0.5,0),0.5)]

def run(size=2,resolution=100,mag=0.1,waves=DEFAULT_WAVES):
    point_array = intensity_array(waves,(resolution,resolution),mag,resolution / size)
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.mesh.primitive_plane_add(size)
    me = bpy.context.active_object.data
    bm = bmesh.new()
    minimum_coordinate = size / -2
    increment = size / resolution
    bmesh.ops.delete(bm, geom=bm.verts)
    for x in range(resolution):
        for y in range(resolution):
            x_co = x * increment + minimum_coordinate
            y_co = y * increment + minimum_coordinate
            bmesh.ops.create_vert(bm, co=(x_co, y_co, point_array[x][y]))
            bm.verts.ensure_lookup_table()
            if x>0 and y>0:
                face_verts = [bm.verts[x*resolution+y],
                              bm.verts[(x-1)*resolution+y],
                              bm.verts[x*resolution+y-1],
                              bm.verts[(x-1)*resolution+y-1]]
                bmesh.ops.contextual_create(bm, geom=face_verts)
    bm.to_mesh(me)
    bm.free()
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 3
    bpy.context.object.modifiers["Subdivision"].render_levels = 4
    bpy.ops.object.mode_set(mode='OBJECT')

