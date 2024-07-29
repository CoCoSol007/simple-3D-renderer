# Simple 3D Renderer

This is a basic 3D renderer created using Pygame and math.


## Origin

This project is a revised version of an earlier project I created in 2021. It was completed in just two hours without the use of the internet. If you have any ideas, please contact me.

## Calculation mode 

The view has two modes:
- PYTHAGORE (using pythagorean theorem)
- THALES (using thales's theorem) (my favorite)

To create a rendering with a specific mode, use the following syntax:
```python
# init with PYTHAGORE view
renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)

# init with THALES view
renderer = Renderer(400, 400, ViewCamera.THALES)
```

## Usage

In src/main.py you write your code like this:


```python
"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer, ViewCamera

# create the renderer with the size of 400x400
# with the view calculed by PYTHAGORE, you can also chose THALES
renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)

renderer.new_square(0,0,-4, 1, 1, 1)
renderer.new_triangle(1,0,-4, 1, 1, 1)

# launch the renderer
renderer.launch()
```

You can use ZQSD on a French keyboard to move the camera and view the result.

```bash
python main.py
```

## Dependencies


```bash
pip install -r requirements.txt
```
