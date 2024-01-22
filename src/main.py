"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer, ViewCamera

# create the renderer with the size of 400x400
renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)

for x in range(5):
    for y in range(5):
        renderer.new_square(x,y,-4, 1, 1, 1)

renderer.new_square(1,1,4, 1, 1, 1)

# launch the renderer
renderer.launch()