# simple-3d-renderer
It's a simple 3d rederer made with pygame and math


## Origin

This project was a copy of an old project that I made in 2021 in 2 hours without internet.
Also I know it is not perfect but if you have any idea please contact me.

## Usage

in =main you write your code like this:


```python
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
```

You will be able to use ZQSD (french keyboard) to move the camera and see the result.


```bash
python main.py
```

## Dependencies


```bash
pip install -r requirements.txt
```
