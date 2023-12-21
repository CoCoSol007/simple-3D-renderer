"""The file that regroupe all renderer features"""

import pygame
from renderer.shapes import Point, Square, Shape, Triangle


class Renderer:
    def __init__(self, width: float = 400, height: float = 400) -> None:

        self.camera = Camera(0,0)

        self.velocity = 0.1

        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.run = True

        self.shapes : list[Shape] = []

    # Fonction to add formes
    def new_square(self, x: float = 0, y: float = 0, z: float = 0, width: float = 1, height: float = 1, size: float = 1) -> None:  
        square = Square(Point(x, y, z), width, height, size)
        self.shapes.append(square)

    def new_triangle(self, x: float = 0, y: float = 0, z: float = 0, width: float = 1, height: float = 1, size: float = 1) -> None:
        triangle = Triangle(Point(x, y, z), width, height, size)
        self.shapes.append(triangle)

    def update(self):
        self.update_movement()
        self.draw()
        pygame.display.update()
        self.clock.tick(30)

    def draw(self):
        self.window.fill((0, 255, 255))
        for shape in self.shapes:
            shape.draw(self.window, self.camera)

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

class Camera(Point):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

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
    