"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer, ViewCamera

# create the renderer with the size of 400x400 with the view calculed by PYTHAGORE, you can also chose THALES
renderer = Renderer(400, 400, ViewCamera.THALES)

points = [
    (-1.0, -1.0, -3.5),
    (0.4, 0.0, -5.0),
    (1.0, 1.0, -3.0),
]

renderer.new_mesh(points)

# launch the renderer
renderer.launch()
