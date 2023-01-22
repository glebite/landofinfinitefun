"""ursina_mesh.py
"""
from ursina import *


app = Ursina()
window.title = 'My Game'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

ourMesh = Mesh(vertices=[[0, 0, 0],
                         [1, 0, 0],
                         [1, 0, 1],
                         [0, 0, 1]],
               triangles=[[0, 1, 2, 3]])


ourEntity = Entity(model=ourMesh)


EditorCamera()


app.run()
