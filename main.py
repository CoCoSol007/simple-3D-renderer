# fait par Corentin SOLOIS

from ast import Tuple
import math
import pygame

# Define the initial position of the camera in 3D space.
camera_pos = [0, 5, 0]


def from3Dto2D(xyz: tuple[int,int, int]):
    """
    Convert a 3D point to a 2D point in camera space.

    Args:
        xyz (list): A list representing a 3D point [x, y, z].

    Returns:
        list: A list representing a 2D point [x', y'] in camera space.
              Returns [None, None] if the 3D point is at the camera's position.
    """
    # Extract x, y, and z coordinates from the input.
    x = xyz[0]
    z = xyz[1]
    y = xyz[2]

    # Calculate the vector from the 3D point to the camera position.
    current_x = x - camera_pos[0]
    current_z = z - camera_pos[1]
    current_y = y - camera_pos[2]

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

    return [new_x, new_y]





def generate_cube_edges():
    """
    Generate the edges of a 3D cube.

    Returns:
        list: A list of edges, where each edge is represented as a pair of vertices.
    """
    cube_edges = []

    # Cube vertices
    vertices = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1)
    ]

    # Cube edges (connecting vertices)
    edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)
    ]

    for edge in edges:
        vertex1 = vertices[edge[0]]
        vertex2 = vertices[edge[1]]
        cube_edges.append([vertex1, vertex2])

    return cube_edges


def transform_cube(lst):
    """
    Transform 3D cube coordinates into 2D coordinates.

    Args:
        lst (list): List of 3D edges, where each edge is represented as a pair of vertices.

    Returns:
        list: List of transformed 2D edges, where each edge is represented as a pair of 2D points.
    """
    lst_2D_edge = []
    for edge in lst:
        current_edge = []
        for point in edge:
            current_edge.append(from3Dto2D(point))
        lst_2D_edge.append(current_edge)
    return lst_2D_edge


# Initialize Pygame
pygame.init()

speed = 0.1  # Camera movement speed

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window size
width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Drawing")

clock = pygame.time.Clock()


def draw_line(coordinates):
    """
    Draw a line on the Pygame window based on 2D coordinates.

    Args:
        coordinates (list): List of 2D coordinates [x, y].
    """
    transformed_coords = []  # Create a new list for transformed coordinates
    for coo in coordinates:
        if coo[0] is None:
            return -1
        x = coo[0] * 500 + 200
        y = coo[1] * 500 + 200
        # Add transformed coordinates to the new list
        transformed_coords.append((x, y))
    pygame.draw.line(
        window, WHITE, transformed_coords[0], transformed_coords[1], 1)


def update_movement():
    """
    Update the camera's position based on user input.
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        camera_pos[0] -= speed
    if keys[pygame.K_d]:
        camera_pos[0] += speed
    if keys[pygame.K_z]:
        camera_pos[1] -= speed
    if keys[pygame.K_s]:
        camera_pos[1] += speed
    if keys[pygame.K_SPACE]:
        camera_pos[2] -= speed
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        camera_pos[2] += speed


while True:
    # Update camera movement and cube transformation
    update_movement()
    cube_edges = generate_cube_edges()
    projected_cube_edges = transform_cube(cube_edges)

    # Clear the Pygame window
    window.fill(BLACK)

    # Draw the cube edges
    for coords in projected_cube_edges:
        draw_line(coords)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(30)
