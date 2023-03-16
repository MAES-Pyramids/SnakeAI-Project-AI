from util.point import Point
from util.constants import CONSTANTS
import pygame

class brick(pygame.sprite.Sprite):
    def __init__(self, position: Point) -> None:
        super().__init__()
        self.name = "wall"
        self.image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\obstecal.png").convert_alpha(), CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.position = position

    


class wall:
    def __init__(self) -> None:
        self.body = []
        self.create_wall()
    
    def create_wall(self) -> None:
        for row in range(CONSTANTS.GRID_SIZE[0]):
          for col in range(CONSTANTS.GRID_SIZE[1]):
            if row == 0 or row == CONSTANTS.GRID_SIZE[0] - 1 or col == 0 or col == CONSTANTS.GRID_SIZE[1] - 1:
              self.body.append(brick(Point(row, col)))


