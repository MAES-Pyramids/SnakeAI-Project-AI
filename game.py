import pygame
import numpy as np
from util.constants import CONSTANTS
from util.directions import Direction
from util.point import Point
from sprites.food import Food
from sprites.snake import Snake, Segment


class Game:
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(CONSTANTS.WINDOW_TITLE)
    pygame.display.set_icon(pygame.image.load(r"assets\images\snake.png"))


    def __init__(self) -> None:
        self.game_window = pygame.display.set_mode(
            (CONSTANTS.WINDOW_WIDTH, CONSTANTS.WINDOW_HEIGHT))
        self.grid = np.ndarray(CONSTANTS.GRID_SIZE, object)
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.events = []
        self.steps = []
        self.background = pygame.image.load(r"assets\images\background.jpg")

        self.GAME_OVER = False
        self.play_music()
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
        self.game_window.blit(self.background, (0, 0))
        self.fill_grid()
        self.draw_grid()
        self.display_score()
        self._handle_input()

        # Check if snake head is on the same position as food 
        if self.snake.head.position == self.food.position:
            pygame.mixer.Sound(r"assets\sounds\eat.mp3").play()
            self.snake.grow()
            self.food.spawn()

        # Check if snake head is on the same position as any of the body segments
        if self.snake.length() >= 4 and self.snake.head.position in [seg.position for seg in self.snake.body[:-1]]: 
            pygame.mixer.Sound(r"assets\sounds\crash.mp3").play()
            self.GAME_OVER = True


        
        pygame.display.update()

    def fixed_update(self):
        ticks = pygame.time.get_ticks()
        # All code within this if statment run in fixed time TIME_STEP
        if ticks - self.old_tick > CONSTANTS.TIME_STEP:
            if (self.steps):
                self.snake.change_direction(self.steps.pop(0))
            self.snake.move()
            self.old_tick = ticks
    # -------------Display Score on the screen--------------- #
    def display_score(self):
        font = pygame.font.SysFont('comicsans', 20 , True)
        text = font.render(f"Score: {self.snake.length() - 1}", True, (255, 255, 255))
        self.game_window.blit(text, (10, 10))

    # ------Create a 2D array to store the game objects------ #
    def fill_grid(self):
        self.grid = [[None for col in range(CONSTANTS.GRID_SIZE[1])] for row in range(
            CONSTANTS.GRID_SIZE[0])]
        for seg in self.snake.body:
            self.grid[seg.position.x][seg.position.y] = seg
        self.grid[self.food.position.x][self.food.position.y] = self.food
    # ----------------- Draw the game objects ------------------ #
    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                if cell != None:
                    self.game_window.blit(
                        cell.image, (cell.position.x*CONSTANTS.PIXEL_SIZE[0], cell.position.y*CONSTANTS.PIXEL_SIZE[1]))
                    
    # ------------------ Handle user input ------------------ #
    def _handle_input(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                CONSTANTS.TIME_STEP /= 1.8

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
                CONSTANTS.TIME_STEP = CONSTANTS.default_STEP
    # -----------------Play Background music ---------------- #
    def play_music(self):
        pygame.mixer.music.load(r"assets\sounds\background.mp3")
        pygame.mixer.music.play()

if __name__ == '__main__':
    Game().run()
