from sprites.food import Food
from sprites.obstacles import Obstacles
from sprites.wall import Wall
from .state import State
from queue import Queue
from util.directions import Direction


class BFS:
    def __init__(self, state: State, food: Food, wall: Wall, obstacles: Obstacles) -> None:
        self.state = state
        self.food = food
        self.wall = wall
        self.obstacles = obstacles
        self.frontier = Queue()
        self.visited = set()

    def find_path(self):
        self.frontier.put(self.state)
        self.visited.add(self.state.head)

        while self.frontier.qsize():
            current_state = self.frontier.get()
            if current_state.head == self.food.position:
                return self.get_path(current_state)

            self.get_neighbors(current_state)
        else:
            print("No path found")
    
    # Generates neighbors for the given state
    # A valid neighbor state is that it's not visited before
    # and it doesn't collide with other disallowed sprites (e.g obstacle)
    def get_neighbors(self, state: State):
        directions = [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT]
        for dir in directions:
            new_head = state.head + dir
            if new_head not in self.visited and not self.check_collision(new_head, state):
                self.visited.add(new_head)
                new_state = State(state.body[1:]+[new_head], state, dir)
                self.frontier.put(new_state)
    
    # Generates a path from the goal state until the first state and then reverses the path.
    def get_path(self, goal_state: State):
        path = []
        current = goal_state
        while current.parent:
            path.append(current.direction)
            current = current.parent
        path.reverse()
        return path
    
    # Checks if snake' head position is the same of any sprite position from wall and obstacles
    # Also checks, if the head segment is the same segment of any part of the snake body segments
    def check_collision(self, head, state: State):
        return any(head == sprite.position for sprite in self.wall.sprites+self.obstacles.sprites) or any(head == seg for seg in state.body)
