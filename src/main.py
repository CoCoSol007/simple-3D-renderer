"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer

# create the window with the size of 400x400
window = Renderer(400, 400)

# create a squares 
window.new_square(0,0 ,-4, 1, 1)
window.new_square(1,0 ,-4, 1, 1)

# create a triangle
window.new_triangle(-1,0 ,-4, 1, 1, 1)

# launch the window
window.launch()