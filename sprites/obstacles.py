from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
from .game_object import GameObject
from .object_group import ObjectGroup
import pygame
import random


class Brick(GameObject):
    def __init__(self,
                 position=Point(0, 0),
                 image=pygame.Surface([CONSTANTS.PIXEL_SIZE]*2)) -> None:
        super().__init__(position, image)
        self.image.fill("#FF005C")


class Obstacles(ObjectGroup):
    def __init__(self, num_obstacles: int = 1) -> None:
        super().__init__()
        for i in range(num_obstacles):
            self.create_obstacle()

    def create_obstacle(self) -> None:
        obstacle_body = [Brick(Point.get_random_point())]
        length = random.randint(1, CONSTANTS.Max_Obstacle_length)
        random_direction = Direction.random_direction()
        for i in range(length):
            if i > 4:
                random_direction = Direction.random_direction()
            new_segment = Brick(obstacle_body[-1].position+random_direction)
            obstacle_body.append(new_segment)
        self.add(*obstacle_body)
