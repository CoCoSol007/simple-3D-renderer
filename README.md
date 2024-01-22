# simple-3d-renderer
It's a simple 3d rederer made with pygame and math


## Origin

This project was a copy of an old project that I made in 2021 in 2 hours without internet.
Also I know it is not perfect but if you have any idea please contact me.

## Usage

in =main you write your code like this:


```python
"""The main file of the 3D renderer"""


# import the renderer module
from renderer.renderer import Renderer, ViewCamera

# create the renderer with the size of 400x400 with the view calculed by PYTHAGORE, you can also chose THALES
renderer = Renderer(400, 400, ViewCamera.PYTHAGORE)

renderer.new_square(1,1,-4, 1, 1, 1)

# launch the renderer
renderer.launch()
```

You will be able to use ZQSD (french keyboard) to move the camera and see the result.


```bash
python main.py
```

## Dependencies


```bash
pip install -r requirements.txt
```
