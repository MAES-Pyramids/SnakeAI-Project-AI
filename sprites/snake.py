import sys
sys.path.append('../SnakeAI')
from util.directions import Direction
import pygame
from util.constants import Constants
from util.point import Point

class Segment(pygame.sprite.Sprite):
    def __init__(self, point:Point) -> None:
        super().__init__()
        self.image = pygame.Surface(Constants.PIXEL_SIZE)
        self.image.fill('Green')
        self.rect = self.image.get_rect()
        self.position = point


class Snake:
    def __init__(self) -> None:
        self.body = [Segment(Point(5,5))]
        self.head = self.body[-1]
        self.direction = Direction.RIGHT

    def change_direction(self, new_direction:Direction):
        if new_direction + self.direction != Point(0,0):
            self.direction = new_direction
    
    def move(self):
        new_segment = Segment(self.head.position+self.direction)
        self.head=new_segment
        
        self.body.append(new_segment)
        self.body = self.body[1:]

    def grow(self):
        new_segment =self.body[0]
        self.body.insert(0,new_segment)

    def collides_with(self, other):
        return self.head.rect.colliderect(other)