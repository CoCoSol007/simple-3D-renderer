from enum import Enum


class Camera:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, fov:float = 1, view:"ViewCamera"=1) -> None:
        self.fov = fov
        self.x = x
        self.y = y
        self.z = z

        self.view = view

    def get_pos(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    # Fonctions to move the camera
    def forward(self, velocity: float = 1) -> None:
        self.z -= velocity

    def backward(self, velocity: float = 1) -> None:
        self.z += velocity

    def left(self, velocity: float = 1) -> None:
        self.x -= velocity

    def right(self, velocity: float = 1) -> None:
        self.x += velocity

    def up(self, velocity: float = 1) -> None:
        self.y -= velocity

    def down(self, velocity: float = 1) -> None:
        self.y += velocity

class ViewCamera(Enum):
    PYTHAGORE = 0
    THALES = 1