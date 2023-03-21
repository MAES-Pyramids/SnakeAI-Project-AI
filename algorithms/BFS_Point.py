from util.point import Point
from util.directions import Direction
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
            self.get_neighbors(current_position, current_path,snake ,wall, obstacles)

        print("No path found")

    def get_neighbors(self, current_position: Point, current_path: list,snake:Snake ,wall: Wall, obstacles: Obstacles):
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

            # Check if new_position is already in the current path or visited set
            if new_position in current_path or new_position in self.visited:
                continue
            
            # Check if new_position is outside the boundaries of the game board
            # if snake.collides_with(wall.sprites):
            #     continue
            
            # Check if new_position is inside the obstacles
            # if snake.collides_with(obstacles.sprites):
            #     continue
            
            # Check if new_position is inside the snake
            # if new_position in snake.sprites:
            #     continue

            self.our_queue.put(current_path + [new_position])

    
