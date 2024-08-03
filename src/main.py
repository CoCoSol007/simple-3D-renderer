"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer, ViewCamera

# create the renderer with the size of 400x400 with the view calculed by PYTHAGORE, you can also chose THALES
renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)

points = [
    (1.2, -3.4, 2.1),
    (-4.5, 0.6, -1.7),
    (3.3, 2.2, -0.4)
]

renderer.new_mesh(points)

# launch the renderer
renderer.launch()
