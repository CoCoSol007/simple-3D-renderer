"""The file that regroupe all renderer features"""

import pygame
from renderer.camera import Camera, ViewCamera
from renderer.shapes import Point, Mesh



class Renderer:
    def __init__(self, width: float = 400, height: float = 400,view:ViewCamera=ViewCamera.PYTHAGORE ) -> None:

        self.camera = Camera(0,0, view=view)

        self.velocity = 0.1

        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.run = True

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False) 

        self.meshes : list[Mesh] = []

    def new_mesh(self, points: list[tuple[float, float, float]]):
        self.meshes.append(Mesh([Point(x, y, z) for x, y, z in points]))

    def update(self):
        self.camera.update_rotation_matrix()
        self.update_movement()
        self.draw()
        pygame.display.update()
        self.clock.tick(30)

    def draw(self):
        self.window.fill((0, 255, 255))
        for mesh in self.meshes:
            mesh.draw(self.window, self.camera)

    def update_movement(self):
        """
        Update the camera's position based on user input.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_LEFT] or keys[pygame.K_a]: 
            self.camera.left(self.velocity)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.camera.right(self.velocity)
        if keys[pygame.K_z] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.camera.forward(self.velocity)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.camera.backward(self.velocity)
        if keys[pygame.K_SPACE]:
            self.camera.up(self.velocity)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.camera.down(self.velocity)

        self.camera.rotate_y( pygame.mouse.get_rel()[0] * self.camera.velocity)

    def launch(self):
        while self.run:

            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False 

        pygame.quit()
