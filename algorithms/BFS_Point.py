from util.point import Point
from util.directions import Direction
from util.constants import CONSTANTS
from sprites.obstacles import Obstacles
from sprites.snake import Snake
from sprites.wall import Wall
from queue import Queue

class BFS:
    def __init__(self):
        self.visited = set()
        self.our_queue = Queue()

    def find_path(self, snake: Snake, food_position: Point, wall: Wall, obstacles: Obstacles):
        snake_position = snake.head.position
        self.visited.clear()
        self.our_queue = Queue()
        self.our_queue.put([snake_position])

        while not self.our_queue.empty():
            current_path = self.our_queue.get()
            current_position = current_path[-1]

            if current_position == food_position:
                return self.return_path(current_path)

            if current_position in self.visited:
                continue

            self.visited.add(current_position)
            self.get_neighbors(current_position, current_path, snake, wall, obstacles)

        print("No path found")
        return []

    def get_neighbors(self, current_position: Point, current_path: list, snake: Snake, wall: Wall, obstacles: Obstacles):
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            new_position = Point(current_position.x + dx, current_position.y + dy)

            if (new_position in current_path) or (new_position in self.visited):
                continue

            if (new_position.x <= 0) or (new_position.y <= 0) or (new_position.x >= CONSTANTS.WINDOW_WIDTH) or (new_position.y >= CONSTANTS.WINDOW_HEIGHT):
                continue

            if any(sprite.position == new_position for sprite in wall.sprites + obstacles.sprites + snake.sprites[1:]):
                continue

            self.our_queue.put(current_path + [new_position])

    def return_path(self, direction_list: list):
        directions = []
        for i in range(1, len(direction_list)):
            prev_pos, curr_pos = direction_list[i - 1], direction_list[i]
            if curr_pos.x > prev_pos.x:
                directions.append(Direction.RIGHT)
            elif curr_pos.x < prev_pos.x:
                directions.append(Direction.LEFT)
            elif curr_pos.y > prev_pos.y:
                directions.append(Direction.DOWN)
            elif curr_pos.y < prev_pos.y:
                directions.append(Direction.UP)
        return directions
