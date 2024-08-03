import math
import pygame
import numpy as np
from renderer.camera import Camera, ViewCamera
class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0,  fov: float = 1) -> None:
        self.x = x
        self.y = y
        self.z = z

        self.fov = fov


    def to_2d(self, camera: "Camera", width: float = 400, height: float = 400) -> pygame.math.Vector2 | None:
        # Get the view matrix from the camera
        view_matrix = camera.get_view_matrix()

        # Transform the point using the view matrix
        point_3d = np.array([self.x, self.y, self.z, 1])
        transformed_point = view_matrix @ point_3d

        current_x = transformed_point[0]
        current_y = transformed_point[1]
        current_z = transformed_point[2]

        if camera.view == ViewCamera.THALES:
            fov = -camera.fov

            if current_z >= 0:
                return None

            new_x = current_x * fov / current_z
            new_y = current_y * fov / current_z

            return pygame.math.Vector2(new_x * 500 + width / 2, new_y * 500 + height / 2)

        elif camera.view == ViewCamera.PYTHAGORE:

            if current_z >= 0:
                return None

            vector3D_pointToCam = current_x * current_x + \
                current_y * current_y + current_z * current_z
            vector3D_pointToCam = math.sqrt(vector3D_pointToCam)

            if vector3D_pointToCam <= 0:
                return None

            # Calculate the 2D coordinates (x', y') in camera space.
            new_x = current_x / vector3D_pointToCam
            new_y = current_y / vector3D_pointToCam

            return pygame.math.Vector2(new_x * 500 + width / 2, new_y * 500 + height / 2)


class Mesh:
    def __init__(self, points: list[Point]) -> None:
        if len(points) != 3:
            raise ValueError("Mesh must have 3 points")
        self.points = points

    def moyenne_x(self) -> float:
        return sum(point.x for point in self.points) / len(self.points)

    def moyenne_y(self) -> float:
        return sum(point.y for point in self.points) / len(self.points)

    def moyenne_z(self) -> float:
        return sum(point.z for point in self.points) / len(self.points)

    def distance_to_camera(self, camera: Camera) -> float:
        # Calculate the distance from the first vertex of the mesh to the camera.
        return math.sqrt(
            (self.moyenne_x() - camera.x) ** 2 +
            (self.moyenne_y() - camera.y) ** 2 +
            (self.moyenne_z() - camera.z) ** 2
        )

    def color_from_distance(self, distance: float) -> tuple:

        def sigmoid(x, scale=1):
            return 1 / (1 + math.exp(-x * scale))

        midpoint = 500.0
        scaling_factor = 1

        t = sigmoid( (distance - midpoint), scaling_factor)

        min_distance = 0.0
        max_distance = 100.0

        t = max(0, min((distance - min_distance) / (max_distance - min_distance), 1))

        return (255 * (1-t), 255 * (1-t) , 255 * (1-t))

    def draw(self, window: pygame.Surface, camera: Camera) -> None:
            distance = self.distance_to_camera(camera)
            color = self.color_from_distance(distance)

            point_list = [point.to_2d(camera, window.get_width(), window.get_height()) for point in self.points]
            if None not in point_list:
                # Filter out None values from point_list
                filtered_point_list = [point for point in point_list if point is not None]
                
                # Draw the polygon with the filtered point list
                pygame.draw.polygon(window, color, filtered_point_list)
                pygame.draw.polygon(window, (0, 0, 0), filtered_point_list, 1)
