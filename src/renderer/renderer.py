"""The file that regroupe all renderer features"""

import math
import pygame


class Renderer:
    def __init__(self, width: float = 400, height: float = 400) -> None:

        self.camera = Camera(0,0)

        self.velocity = 0.1

        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.run = True

    def update(self):
        self.update_movement()

        print(self.camera.get_pos())

    def update_movement(self):
        """
        Update the camera's position based on user input.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.camera.left(self.velocity)
        if keys[pygame.K_d]:
            self.camera.right(self.velocity)
        if keys[pygame.K_z]:
            self.camera.forward(self.velocity)
        if keys[pygame.K_s]:
            self.camera.backward(self.velocity)
        if keys[pygame.K_SPACE]:
            self.camera.up(self.velocity)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.camera.down(self.velocity)

    def launch(self):
        while self.run:

            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def to_2d(self, camera:"Camera") -> tuple[float, float]:
        """
        Convert a 3D point to a 2D point in camera space.
        Returns:
            list: A list representing a 2D point [x', y'] in camera space.
                Returns [None, None] if the 3D point is at the camera's position.
        """

         # Calculate the vector from the 3D point to the camera position.
        current_x = self.x - camera.x
        current_z = self.z - camera.z
        current_y = self.y - camera.y

        if current_z >= 0:
            return [None, None]

        # Calculate the magnitude of the vector from the 3D point to the camera.
        vector3D_pointToCam = current_x * current_x + \
            current_y * current_y + current_z * current_z
        vector3D_pointToCam = math.sqrt(vector3D_pointToCam)

        # Check if the 3D point coincides with the camera position.
        if vector3D_pointToCam <= 0:
            return [None, None]

        # Calculate the 2D coordinates (x', y') in camera space.
        new_x = current_x / vector3D_pointToCam
        new_y = current_y / vector3D_pointToCam

        return (new_x, new_y)


class Camera(Point):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_pos(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    # Fonctions to move the camera
    def forward(self, velocity: float = 1) -> None:
        self.x += velocity
    
    def backward(self, velocity: float = 1) -> None:
        self.x -= velocity

    def left(self, velocity: float = 1) -> None:
        self.y -= velocity

    def right(self, velocity: float = 1) -> None:
        self.y += velocity

    def up(self, velocity: float = 1) -> None:
        self.z -= velocity

    def down(self, velocity: float = 1) -> None:
        self.z += velocity
    