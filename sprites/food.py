import random
from helper.point import POINT
import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = ...
        self.rect = ...
        self.position = ...

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def spawn(self) -> None:
        pass

    def get_pos(self) -> POINT:
        pass
