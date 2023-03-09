from util.point import Point
from util.constants import CONSTANTS
import pygame
import random


class Food(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\food.png"), CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.position = Point(0, 0)
        self.spawn()

    def spawn(self) -> None:
        self.position = Point.get_random_point()
