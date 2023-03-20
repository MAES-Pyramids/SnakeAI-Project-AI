import pygame
import time
import numpy as np
from algorithms.BFS import BFS
from util.constants import CONSTANTS
from util.directions import Direction
from util.point import Point
from sprites.food import Food
from sprites.snake import Snake, Segment
from sprites.obstacles import Obstacles
from sprites.wall import Wall
from sprites.particle import Particle
from sprites.game_object import GameObject
from algorithms.state import State


class Game:
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(CONSTANTS.WINDOW_TITLE)
    pygame.display.set_icon(pygame.image.load(r"assets\images\snake.png"))

    def __init__(self) -> None:
        self.game_window = pygame.display.set_mode((CONSTANTS.WINDOW_WIDTH, CONSTANTS.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.Obstacles = Obstacles(CONSTANTS.NUM_OBSTACLES)
        self.snake = Snake()
        self.food = Food()
        self.wall = Wall()
        self.particles = Particle()
        self.game_objects = [self.snake, self.food, self.wall, self.Obstacles]
        self.events = []
        self.steps = []
        self.eated = False
        self.GAME_OVER = False
        self.RUSH = 0
        self.old_tick = 0
        # self.play_music()

    # game loop
    def run(self) -> None:
        while not self.GAME_OVER:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.fixed_update()
            self.update()

    def update(self) -> None:
        self.clock.tick(CONSTANTS.FPS)
        self.game_window.fill('#0A1931')
        self._draw_map()
        self._display_score()
        self._handle_input()
        self.particles.emit(self.game_window, "#FFC947")
        self.check_collison()
        pygame.display.update()

    def fixed_update(self):
        ticks = pygame.time.get_ticks()
        # All code within this if statment run in fixed time TIME_STEP
        if ticks - self.old_tick > CONSTANTS.TIME_STEP:
            if (self.steps):
                self.snake.change_direction(self.steps.pop(0))
            self.snake.move(self.eated)
            self.old_tick = ticks
            self.eated = False

    # -------------Display Score on the screen--------------- #
    def _display_score(self):
        font = pygame.font.SysFont('comicsans', 20, True)
        text = font.render(
            f"Score: {len(self.snake) - 1}", True, (255, 255, 255))
        self.game_window.blit(text, (10, 10))

    def check_collison(self):
        # Check if snake head is on the same position as food
        if self.snake.collides_with(self.food):
            self.eated = True
            self.particles.add_particles(
                self.food.position.x, self.food.position.y)
            pygame.mixer.Sound(r"assets\sounds\eat.mp3").play()
            self.food.spawn()

        # Check if snake head is on the same position as any of the body segments
        if self.snake.collides_with(self.snake):
            pygame.mixer.Sound(r"assets\sounds\crash.mp3").play()
            time.sleep(1)
            self.GAME_OVER = True

        # Check if snake head is on the same position as any of the wall
        if self.snake.collides_with(self.wall):
            pygame.mixer.Sound(r"assets\sounds\crash.mp3").play()
            time.sleep(1)
            self.GAME_OVER = True

        # Check if snake head is on the same position as any of the Obstacles
        if self.snake.collides_with(self.Obstacles):
            pygame.mixer.Sound(r"assets\sounds\crash.mp3").play()
            time.sleep(1)
            self.GAME_OVER = True

    # ----------------- Draw the game objects ------------------ #
    def _draw_map(self):
        for object in self.game_objects:
            object.draw(self.game_window)

    # ------------------ Handle user input ------------------ #
    def _handle_input(self):
        self.steps.extend(BFS.find_path(State(self.snake, self.food, self.wall, self.Obstacles, [])))
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                self.RUSH += 1
                if self.RUSH == 1:  # only speed up if there is at least one key pressed
                    CONSTANTS.TIME_STEP /= 2

                action = event.key
                match action:
                    case pygame.K_UP:
                        self.steps.append(Direction.UP)
                    case pygame.K_DOWN:
                        self.steps.append(Direction.DOWN)
                    case pygame.K_LEFT:
                        self.steps.append(Direction.LEFT)
                    case pygame.K_RIGHT:
                        self.steps.append(Direction.RIGHT)

            if event.type == pygame.KEYUP:
                self.RUSH -= 1
                if self.RUSH == 0:  # bring back the old speed if there is no pressed key
                    CONSTANTS.TIME_STEP *= 2

    # -----------------Play Background music ---------------- #

    def play_music(self):
        pygame.mixer.music.load(r"assets\sounds\background.mp3")
        pygame.mixer.music.play()


if __name__ == '__main__':
    Game().run()
