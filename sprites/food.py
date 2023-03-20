from util.point import Point
from util.constants import CONSTANTS
from sprites.game_object import GameObject
import pygame


class Food(GameObject):
    def __init__(self,
                 position=Point(0, 0),
                 image=pygame.Surface([CONSTANTS.PIXEL_SIZE]*2)) -> None:
        super().__init__(position, image)
        self.image.fill("#FFC947")
        self.spawn()

    def spawn(self) -> None:
        self.position = Point.get_random_point()
        self.update_rect()
