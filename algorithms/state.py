from copy import copy
from sprites.food import Food
from sprites.snake import Snake
from sprites.obstacles import Obstacles
from sprites.wall import Wall
from util.point import Point


class State:
    def __init__(self, snake, parent: 'State' = None, direction=None) -> None:
        if isinstance(snake, Snake):
            self.body = self.get_snake_body(snake)
        else:
            self.body = snake
        self.head = self.body[-1]
        self.parent = parent
        self.direction = direction

    def get_snake_body(self, snake: Snake):
        return [sprite.position for sprite in snake.sprites]

    def __hash__(self) -> int:
        return hash(self.head)

    def __eq__(self, other: 'State'):
        return self.head == other.head
