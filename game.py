import pygame
import numpy as np
from util.constants import CONSTANTS
from util.directions import Direction
from util.point import Point
from sprites.food import Food
from sprites.snake import Snake, Segment


class Game:
    pygame.init()
    pygame.display.set_caption(CONSTANTS.WINDOW_TITLE)

    def __init__(self) -> None:
        self.game_window = pygame.display.set_mode(
            (CONSTANTS.WINDOW_WIDTH, CONSTANTS.WINDOW_HEIGHT))
        self.events = []
        self.steps = []
        self.snake = Snake()
        self.food = Food()
        self.GAME_OVER = False
        self.grid = np.ndarray(CONSTANTS.GRID_SIZE, object)
        self.clock = pygame.time.Clock()
        self.old_tick = 0

    # game loop
    def run(self) -> None:
        while not self.GAME_OVER:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.update()
            self.fixed_update()

    def update(self) -> None:
        self.clock.tick(CONSTANTS.FPS)
        self.game_window.fill('black')
        self.fill_grid()
        self.draw_grid()
        self._handle_input()
        if self.snake.head.position == self.food.position:
            self.snake.grow()
            self.food.spawn()
        pygame.display.update()

    def fixed_update(self):
        ticks = pygame.time.get_ticks()
        # All code within this if statment run in fixed time TIME_STEP
        if ticks - self.old_tick > CONSTANTS.TIME_STEP:
            if (self.steps):
                self.snake.change_direction(self.steps.pop(0))
            self.snake.move()
            self.old_tick = ticks

    def fill_grid(self):
        self.grid = [[None for col in range(CONSTANTS.GRID_SIZE[1])] for row in range(
            CONSTANTS.GRID_SIZE[0])]
        for seg in self.snake.body:
            self.grid[seg.position.x][seg.position.y] = seg
        self.grid[self.food.position.x][self.food.position.y] = self.food

    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                if cell != None:
                    self.game_window.blit(
                        cell.image, (cell.position.x*CONSTANTS.PIXEL_SIZE[0], cell.position.y*CONSTANTS.PIXEL_SIZE[1]))

    def _handle_input(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                action = event.key
                match action:
                    case pygame.K_w:
                        self.steps.append(Direction.UP)
                    case pygame.K_s:
                        self.steps.append(Direction.DOWN)
                    case pygame.K_a:
                        self.steps.append(Direction.LEFT)
                    case pygame.K_d:
                        self.steps.append(Direction.RIGHT)


if __name__ == '__main__':
    Game().run()
