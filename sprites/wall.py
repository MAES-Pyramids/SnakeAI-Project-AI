from util.point import Point
from util.constants import CONSTANTS
from sprites.game_object import GameObject
import pygame


class Brick(GameObject):
    def __init__(self, position: Point) -> None:
        name = "wall"
        image = pygame.Surface(CONSTANTS.PIXEL_SIZE)
        super().__init__(name, image, position)
        image.fill("#FF005C")


class Wall:
    def __init__(self) -> None:
        self.body = []
        self.create_wall()

    def create_wall(self) -> None:
        for row in range(CONSTANTS.GRID_SIZE[0]):
            for col in range(CONSTANTS.GRID_SIZE[1]):
                if row == 0 or row == CONSTANTS.GRID_SIZE[0] - 1 or col == 0 or col == CONSTANTS.GRID_SIZE[1] - 1:
                    self.body.append(Brick(Point(row, col)))
