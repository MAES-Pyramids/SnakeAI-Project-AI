from util.constants import CONSTANTS
from util.point import Point
from .state import State
from queue import Queue
from util.directions import Direction
from copy import copy


class BFS:
    frontier = Queue()
    visited = []

    @staticmethod
    def find_path(state: State):
        BFS.frontier = Queue()
        BFS.visited = []
        BFS.frontier.put(state)
        while BFS.frontier.qsize():
            current_state = BFS.frontier.get()
            if current_state.snake.collides_with(current_state.food):
                return current_state.path

            if current_state in BFS.visited:
                continue

            BFS.visited.append(current_state)
            BFS.get_neighbors(current_state)
        print("No path found")


    @staticmethod
    def get_neighbors(state: State):
        directions = [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT]
        for direction in directions:
            # if state.snake.direction + direction == Point(0, 0):
            #     continue
            new_state = copy(state)
            new_state.snake.change_direction(direction)
            new_state.snake.move()
            if new_state.snake.collides_with(new_state.wall)  or new_state.snake.collides_with(state.snake) or new_state.snake.collides_with(new_state.obstacles):
                continue
            new_state.path.append(direction)
            BFS.frontier.put(new_state)
