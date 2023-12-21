"""The main file of the 3D renderer"""

from renderer.renderer import Renderer

window = Renderer(4000, 4000)
window.new_triangle(1, 1, 0, 1, 1, 1)
window.new_square(2, 1, 0, 1, 1, 1)
window.launch()