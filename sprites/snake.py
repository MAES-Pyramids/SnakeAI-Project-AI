from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
from sprites.game_object import GameObject
import pygame


class Segment(GameObject):
    def __init__(self, position: Point) -> None:
        name = "snake"
        image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\segment.png").convert_alpha(), [CONSTANTS.PIXEL_SIZE]*2)
        super().__init__(name, image, position)


class Snake:
    def __init__(self) -> None:
        self.body = [Segment(Point.get_random_point())]
        self.head = self.body[-1]
        self.direction = Direction.RIGHT

    def length(self) -> int:
        return len(self.body)

    def change_direction(self, new_direction: Direction) -> None:
        if new_direction + self.direction != Point(0, 0):
            self.direction = new_direction

    def move(self) -> None:
        new_segment = Segment(self.head.position+self.direction)
        self.head = new_segment

        self.body.append(new_segment)
        self.body = self.body[1:]

    def grow(self) -> None:
        new_segment = self.body[0]
        self.body.insert(0, new_segment)

    def draw(self, surf: pygame.Surface) -> None:
        for seg in self.body:
            seg.draw(surf)

    def collides_with(self, other: object) -> bool:
        return self.head.rect.colliderect(other)
