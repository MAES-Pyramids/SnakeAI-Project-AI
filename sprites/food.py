from util.point import Point
from util.constants import CONSTANTS
from sprites.game_object import GameObject
import pygame


class Food(GameObject):
    def __init__(self) -> None:
        name = "snake"
        image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\food.png"), CONSTANTS.PIXEL_SIZE)
        position = Point(0, 0)
        super().__init__(name, image, position)
        self.spawn()

    def spawn(self) -> None:
        self.position = Point.get_random_point()
