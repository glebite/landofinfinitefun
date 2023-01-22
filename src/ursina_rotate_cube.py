"""
Playing with displaying textures, etc...
"""
from ursina import *
import time


app = Ursina()
window.title = "Hello there."

blammo = Entity(model="objs/untitled.obj", color=color.white, scale=0.5, texture="brick")
blammo.set_position((-2,-1,0))
redcube = Entity(model="cube", scale=0.5, color=color.red, texture="brick")
redcube.set_position((2,1,0))
bluesphere = Entity(model="sphere", texture="textures/blogpost")


def update():
    bluesphere.rotation_x += 30 * time.dt
    bluesphere.rotation_z += 30 * time.dt
    redcube.rotation_y += 30 * time.dt
    redcube.rotation_z += 30 * time.dt
    blammo.rotation_x -= 15 * time.dt
    blammo.rotation_y -= 15 * time.dt


app.run()
