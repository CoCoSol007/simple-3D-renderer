from enum import Enum
import numpy as np

class ViewCamera(Enum):
    PYTHAGORE = 0
    THALES = 1

class Camera:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, fov: float = 1, view: ViewCamera = ViewCamera.PYTHAGORE) -> None:
        self.fov = fov
        self.x = x
        self.y = y
        self.z = z
        self.view = view
        self.velocity = 0.001

        self.y_rotation = 0.0

    def update_rotation_matrix(self) -> None:
        cos_theta = np.cos(self.y_rotation)
        sin_theta = np.sin(self.y_rotation)
        self.rotation = np.array([
            [cos_theta, 0, sin_theta],
            [0, 1, 0],
            [-sin_theta, 0, cos_theta]
        ])

    def get_pos(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    # Fonctions to move the camera
    def forward(self, velocity: float = 1) -> None:
        forward_direction = self.rotation[:, 2]

        self.z -= forward_direction[2] * velocity
        self.y += forward_direction[1] * velocity
        self.x += forward_direction[0] * velocity

    def backward(self, velocity: float = 1) -> None:
        self.forward(-velocity)

    def left(self, velocity: float = 1) -> None:
        left_direction = self.rotation[:, 0]
        self.x -= left_direction[0] * velocity
        self.y += left_direction[1] * velocity
        self.z += left_direction[2] * velocity

    def right(self, velocity: float = 1) -> None:
        self.left(-velocity)

    def up(self, velocity: float = 1) -> None:
        self.y -= velocity

    def down(self, velocity: float = 1) -> None:
        self.y += velocity

    def rotate_y(self, angle):
        self.y_rotation += angle


    def get_view_matrix(self):
        position = np.array([self.x, self.y, self.z])
        view_matrix = np.identity(4)
        translation_to_origin = np.identity(4)
        translation_to_origin[:3, 3] = -position
        view_matrix[:3, :3] = self.rotation
        view_matrix = view_matrix @ translation_to_origin
        return view_matrix