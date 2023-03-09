from util.point import Point
from util.constants import CONSTANTS
import pygame


class Wall(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\Wall.jpg"), CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
