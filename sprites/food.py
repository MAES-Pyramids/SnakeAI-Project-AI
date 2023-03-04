import random
from helper.point import POINT
import pygame


class Food:
    def __init__(self) -> None:
        self.position = ...
        self.rect = ...

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def spawn(self) -> None:
        pass

    def get_pos(self) -> POINT:
        pass
