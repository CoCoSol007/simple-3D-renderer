"""The main file of the 3D renderer"""

from renderer.renderer import Renderer

window = Renderer(400, 400)
window.new_square(1,1 ,1, 1, 1)
window.new_square(2,1 ,1, 1, 1)
window.launch()