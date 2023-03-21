from util.point import Point
from queue import Queue
from util.directions import Direction
from util.constants import CONSTANTS


class BFS:
    def __init__(self):
        self.visited = set()
        self.our_queue = Queue()

    def find_path(self, snake_position: Point, food_position: Point):
        self.visited = set()
        self.our_queue = Queue()
        self.our_queue.put([snake_position])

        while not self.our_queue.empty():
            current_path = self.our_queue.get()
            current_position = current_path[-1]

            if current_position == food_position:
                return current_path

            if current_position in self.visited:
                continue

            self.visited.add(current_position)
            self.get_neighbors(current_position, current_path)

        print("No path found")

    def get_neighbors(self, current_position: Point, current_path: list):
        directions = [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT]

        for direction in directions:
            if direction == Direction.UP:
                new_position = Point(current_position.x, current_position.y - 1)
            elif direction == Direction.DOWN:
                new_position = Point(current_position.x, current_position.y + 1)
            elif direction == Direction.RIGHT:
                new_position = Point(current_position.x + 1, current_position.y)
            elif direction == Direction.LEFT:
                new_position = Point(current_position.x - 1, current_position.y)
            else:
                continue

            # Check if new_position is outside the boundaries of the game board
            if new_position.x < 0 or new_position.y < 0:
                continue
            if new_position.x >= 800 or new_position.y >= 600:
                continue

            # Check if new_position is already in the current path or visited set
            if new_position in current_path or new_position in self.visited:
                continue

            self.our_queue.put(current_path + [new_position])

    
