import sys
sys.path.append('../SnakeAI')
from util.point import Point
from util.constants import CONSTANTS
import pygame
import random


class Food(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface(CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.image.fill('Red')
        self.position = Point(0, 0)
        self.spawn()

    def spawn(self) -> None:
        self.position = Point(
            random.randint(0, CONSTANTS.GRID_SIZE[0]-1),
            random.randint(0, CONSTANTS.GRID_SIZE[1]-1),
        )
