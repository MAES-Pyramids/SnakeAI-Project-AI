from util.point import Point
from util.constants import CONSTANTS
from .game_object import GameObject
from .object_group import ObjectGroup
import pygame


class Brick(GameObject):
    def __init__(self, position=Point(0, 0),
                 image=pygame.Surface([CONSTANTS.PIXEL_SIZE]*2)) -> None:
        super().__init__(position, image)
        image.fill("#FF005C")


class Wall(ObjectGroup):
    def __init__(self) -> None:
        super().__init__()
        self.create_wall()

    def create_wall(self) -> None:
        for row in range(CONSTANTS.GRID_SIZE[0]):
            for col in range(CONSTANTS.GRID_SIZE[1]):
                if row == 0 or row == CONSTANTS.GRID_SIZE[0] - 1 or col == 0 or col == CONSTANTS.GRID_SIZE[1] - 1:
                    self.add(Brick(Point(row, col)))
