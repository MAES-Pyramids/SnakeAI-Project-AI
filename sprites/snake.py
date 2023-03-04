from helper.direction import DIRECTION
from helper.point import POINT
import pygame


class Segment:
    def __init__(self, position: POINT) -> None:
        self.position = ...
        self.rect = ...

    def get_position(self) -> POINT:
        pass


class Snake:
    def __init__(self) -> None:
        self.direction = ...
        self.body = ...

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def move(self, speed: float) -> None:
        pass

    def get_head(self) -> Segment:
        pass

    def get_body(self) -> list[Segment]:
        pass

    def grow(self) -> None:
        pass

    def change_direction(self, direction: DIRECTION) -> None:
        pass

    def collides_with(self, other: pygame.Rect) -> bool:
        pass
