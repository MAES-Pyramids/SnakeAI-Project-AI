from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
from sprites.game_object import GameObject
import pygame
import random


class brick(GameObject):
    def __init__(self, position: Point) -> None:
        name = "brick"
        image = pygame.Surface([CONSTANTS.PIXEL_SIZE]*2)
        super().__init__(name, image, position)
        self.image.fill("#FF005C")


class obstacles(pygame.sprite.Group):
    def __init__(self, num_obstacles: int = 1) -> None:
        super().__init__()
        for i in range(num_obstacles):
            self.create_obstacle()

    def create_obstacle(self) -> None:
        obstacle_body = [brick(Point.get_random_point())]
        length = random.randint(1, CONSTANTS.Max_Obstacle_length)
        random_direction = Direction.random_direction()
        for i in range(length):
            if i > 4:
                random_direction = Direction.random_direction()
            new_segment = brick(obstacle_body[-1].position+random_direction)
            obstacle_body.append(new_segment)
        self.add(obstacle_body)
