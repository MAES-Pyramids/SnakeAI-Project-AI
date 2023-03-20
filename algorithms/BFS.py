from util.constants import CONSTANTS
from util.point import Point
from .state import State
from queue import Queue
from util.directions import Direction
from copy import copy
import numpy as np


class BFS:
    frontier = Queue()
    visited = []
    grid = np.zeros(CONSTANTS.GRID_SIZE)

    @staticmethod
    def find_path(state: State):
        BFS.frontier = Queue()
        BFS.visited = []
        BFS.frontier.put(state)
        while BFS.frontier.qsize():
            current_state = BFS.frontier.get()
            if current_state.snake.collides_with(current_state.food):
                return current_state.path

            BFS.grid[current_state.snake.head.position.x, current_state.snake.head.position.y] = 1

            if current_state in BFS.visited:
                continue

            print(BFS.grid.transpose(), end="\n \n")
            BFS.visited.append(current_state)

            BFS.get_neighbors(current_state)
        else:
            print("HIOII")

    @staticmethod
    def get_neighbors(state: State):
        directions = [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT]
        for direction in directions:
            if state.snake.direction + direction == Point(0, 0):
                continue
            new_state = copy(state)
            new_state.snake.change_direction(direction)
            new_state.snake.move()
            if new_state.snake.collides_with(new_state.wall) or new_state.snake.collides_with(new_state.obstacles) or new_state.snake.collides_with(state.snake):
                continue
            new_state.path.append(direction)
            BFS.frontier.put(new_state)
