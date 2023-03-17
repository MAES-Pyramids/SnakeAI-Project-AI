from util.point import Point
from util.constants import CONSTANTS
from pygame.sprite import Sprite
import pygame


class GameObject(Sprite):
    def __init__(self, name, image, position: Point) -> None:
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.position = position

    def draw(self, surf: pygame.Surface) -> None:
        surf.blit(self.image, (self.position.x * CONSTANTS.PIXEL_SIZE,
                  self.position.y * CONSTANTS.PIXEL_SIZE))
