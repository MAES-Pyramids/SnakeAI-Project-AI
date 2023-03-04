import pygame
from helper.constants import CONSTANTS
from helper.direction import DIRECTION
from helper.point import POINT
from sprites.snake import Snake
from sprites.food import Food


class Game:
    pygame.init()
    pygame.display.set_caption(CONSTANTS.WINDOW_TITLE)

    def __init__(self) -> None:
        self.GAME_OVER = False
        self.game_windows = pygame.display.set_mode(
            (CONSTANTS.WINDOW_WIDTH, CONSTANTS.WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        # Game Loop
        while not self.GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            clock.tick(CONSTANTS.FPS)

    def reset(self):
        pass

    def _handle_user_input(self) -> None:
        pass

    def draw_score(self) -> None:
        pass
