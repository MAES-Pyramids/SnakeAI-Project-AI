from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
from sprites.game_object import GameObject
from copy import copy
import pygame


class Segment(GameObject):
    def __init__(self, position: Point) -> None:
        name = "snake"
        image = pygame.transform.smoothscale(pygame.image.load(r"assets\images\segment.png").convert_alpha(), [CONSTANTS.PIXEL_SIZE]*2)
        super().__init__(name, image, position)


class Snake(pygame.sprite.Group):

    def __init__(self, direction=Direction.RIGHT) -> None:
        super().__init__()
        self.add(Segment(Point(CONSTANTS.GRID_SIZE[0]/2, CONSTANTS.GRID_SIZE[1]/2)))
        self.head = self.sprites()[-1]
        self.direction = direction

    def change_direction(self, new_direction: Direction) -> None:
        if new_direction + self.direction != Point(0, 0):
            self.direction = new_direction

    def move(self, grow: bool) -> None:
        new_segment = Segment(self.head.position+self.direction)
        self.head = new_segment

        self.add(new_segment)
        if not grow:
            self.remove(self.sprites()[0])

    def collides_with(self, other) -> bool:
        if isinstance(other, pygame.sprite.Sprite):
            return self.head.rect.colliderect(other.rect)
        elif isinstance(other, pygame.sprite.Group):
            collision = False
            for sprite in other.sprites()[:-1]:
                if self.collides_with(sprite):
                    collision = True
            return collision
