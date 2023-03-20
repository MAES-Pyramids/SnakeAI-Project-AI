from copy import copy
from sprites.food import Food
from sprites.snake import Snake
from sprites.obstacles import Obstacles
from sprites.wall import Wall


class State:
    def __init__(self, snake: Snake, food: Food, wall: Wall, obstacles: Obstacles, path) -> None:
        self.snake = snake
        self.food = food
        self.wall = wall
        self.obstacles = obstacles
        self.path = path

    def __copy__(self):
        return State(copy(self.snake), self.food, self.wall, self.obstacles, self.path[:])

    def __eq__(self, other: 'State'):
        return self.snake.head.position == other.snake.head.position
