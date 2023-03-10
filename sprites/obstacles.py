from util.point import Point
from util.constants import CONSTANTS
from util.directions import Direction
import pygame
import random



class brick(pygame.sprite.Sprite):
    def __init__(self, position: Point) -> None:
        super().__init__()

        self.image = pygame.transform.smoothscale(pygame.image.load(
            r"assets\images\obstecal.png").convert_alpha(), CONSTANTS.PIXEL_SIZE)
        self.rect = self.image.get_rect()
        self.position = position
        
class obstacles:
    def __init__(self, num_obstacles: int = 1) -> None:
        self.body = []
        for i in range(num_obstacles):
            self.create_obstacle()
    
    def create_obstacle(self) -> None:
        obstacle_body = [brick(Point.get_random_point())]
        lenght =  random.randint(1, 8)
        random_direction = Direction.random_direction()
        for i in range(lenght):
            if i > 4:
                random_direction = Direction.random_direction()
            new_segment = brick(obstacle_body[-1].position+random_direction)
            obstacle_body.append(new_segment)
        self.body += obstacle_body


# class obstacles:
#     def __init__(self) -> None:
#         self.body = [brick(Point.get_random_point())]
#         self.grow()
    
#     def grow(self) -> None:
#         lenght =  random.randint(1, 5)
#         for i in range(lenght):
#             random_direction = Direction.random_direction()
#             new_segment = brick(self.body[-1].position+random_direction)
#             self.body.append(new_segment)