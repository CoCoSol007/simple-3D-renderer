import math
import pygame

class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def to_2d(self, camera:"Point", width: float = 400, height: float = 400) -> pygame.math.Vector2|None:

        current_x = self.x - camera.x
        current_z = self.z - camera.z
        current_y = self.y - camera.y

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

        return pygame.math.Vector2(new_x * 500 + width / 2 , new_y * 500 + height / 2)


class Face:
    def __init__(self, points: list[Point]) -> None:
        self.points = points

    def is_face_visible(self, camera: Point) -> bool:
        return True

    
    def moyenne_x(self) -> float:
        return sum(point.x for point in self.points) / len(self.points)
    
    def moyenne_y(self) -> float:
        return sum(point.y for point in self.points) / len(self.points)
    
    def moyenne_z(self) -> float:
        return sum(point.z for point in self.points) / len(self.points)

    def distance_to_camera(self, camera: Point) -> float:
        # Calculate the distance from the first vertex of the face to the camera.
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

    def draw(self, window: pygame.Surface, camera: Point) -> None:
        if self.is_face_visible(camera):
            distance = self.distance_to_camera(camera)
            color = self.color_from_distance(distance)

            point_list = [point.to_2d(camera, window.get_width(), window.get_height()) for point in self.points]
            if None not in point_list:
                pygame.draw.polygon(window, color, point_list)
                pygame.draw.polygon(window, (0, 0, 0), point_list, 1)


class Shape:
    def __init__(self, point: Point = Point(0, 0, 0), width: float = 1, height: float = 1, size: float = 1) -> None:
        self.point = point
        self.width = width
        self.height = height
        self.size = size

        self.faces = self.generate_faces()

    def generate_faces(self):
        pass

    def draw(self, window: pygame.Surface, camera: Point) -> None:
        for face in self.faces:
            face.draw(window, camera)


class Square(Shape):
    def __init__(self, point: Point = Point(0, 0, 0), width: float = 1, height: float = 1, size: float = 1) -> None:
        super().__init__(point, width, height, size)

    def generate_faces(self) -> list[Face]:

        list_of_points = [
            self.point,
            Point(self.point.x + self.width, self.point.y, self.point.z),
            Point(self.point.x + self.width, self.point.y + self.height, self.point.z),
            Point(self.point.x, self.point.y + self.height, self.point.z),
            Point(self.point.x, self.point.y, self.point.z + self.size),
            Point(self.point.x + self.width, self.point.y, self.point.z + self.size),
            Point(self.point.x + self.width, self.point.y + self.height, self.point.z + self.size),
            Point(self.point.x, self.point.y + self.height, self.point.z + self.size),
        ]

        list_of_faces = [
            Face([list_of_points[0], list_of_points[1], list_of_points[2], list_of_points[3]]),
            Face([list_of_points[4], list_of_points[5], list_of_points[6], list_of_points[7]]),
            Face([list_of_points[0], list_of_points[1], list_of_points[5], list_of_points[4]]),
            Face([list_of_points[1], list_of_points[2], list_of_points[6], list_of_points[5]]),
            Face([list_of_points[2], list_of_points[3], list_of_points[7], list_of_points[6]]),
            Face([list_of_points[3], list_of_points[0], list_of_points[4], list_of_points[7]]),
        ]
        return list_of_faces
    

class Triangle(Shape):
    def __init__(self, point: Point = Point(0, 0, 0), width: float = 1, height: float = 1, size: float = 1) -> None:
        super().__init__(point, width, height, size)

    def generate_faces(self) -> list[Face]:
        list_of_points = [
            self.point,
            Point(self.point.x + self.width, self.point.y, self.point.z),
            Point(self.point.x + self.width, self.point.y + self.height, self.point.z),
            Point(self.point.x, self.point.y + self.height, self.point.z),
            Point(self.point.x + 0.5 * self.width, self.point.y + 0.5 * self.height, self.point.z + self.size),
        ]

        # Adjust the order of vertices in each face to make the pyramid point upward
        list_of_faces = [
            Face([list_of_points[0], list_of_points[3], list_of_points[2], list_of_points[1]]),
            Face([list_of_points[0], list_of_points[1], list_of_points[4]]),
            Face([list_of_points[1], list_of_points[2], list_of_points[4]]),
            Face([list_of_points[2], list_of_points[3], list_of_points[4]]),
            Face([list_of_points[3], list_of_points[0], list_of_points[4]]),
        ]

        return list_of_faces