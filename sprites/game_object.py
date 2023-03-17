from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
from pygame.sprite import Sprite
import random


class GameObject(Sprite):
    def __init__(self, name, image, position: Point) -> None:
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.position = position
