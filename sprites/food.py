import sys
sys.path.append('../SnakeAI')
import pygame
from util.constants import Constants
from util.point import Point
import random

class Food(pygame.sprite.Sprite):
    
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface(Constants.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.image.fill('Red')
        self.position = Point(0,0)
        self.spawn()



    def spawn(self):
        self.position = Point(
            random.randint(0, Constants.GRID_SIZE[0]-1),
            random.randint(0, Constants.GRID_SIZE[1]-1),
        )