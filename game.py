import pygame
from util.constants import Constants
from util.directions import Direction
from util.point import Point
from sprites.food import Food
from sprites.snake import Snake, Segment
class Game:
    pygame.init()
    pygame.display.set_caption(Constants.WINDOW_TITLE)

    def __init__(self) -> None:
        self.snake = Snake()
        self.food = Food()
        self.GAME_OVER = False
        self.game_window = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        self.grid = [[None for col in range(Constants.GRID_SIZE[1])] for row in range(Constants.GRID_SIZE[0])]
        self.clock = pygame.time.Clock()
        self.old_tick = 0
        
        #game loop
        while not self.GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    action = event.key
                    match action:
                        case pygame.K_w:
                            self.snake.change_direction(Direction.UP)
                        case pygame.K_s:
                            self.snake.change_direction(Direction.DOWN)
                        case pygame.K_a:
                            self.snake.change_direction(Direction.LEFT)
                        case pygame.K_d:
                            self.snake.change_direction(Direction.RIGHT)
            
            if self.snake.head.position == self.food.position:
                self.snake.grow()
                self.food.spawn()

            self.fill_grid()
            self.game_window.fill('black')
            self.draw_grid()
            ticks = pygame.time.get_ticks()
            if ticks - self.old_tick > 100:
                self.snake.move()
                self.old_tick = ticks
            
            
            pygame.display.update()
            self.clock.tick(60)
            print(ticks)

            

        
    def fill_grid(self):
        self.grid = [[None for col in range(Constants.GRID_SIZE[1])] for row in range(Constants.GRID_SIZE[0])]
        for seg in self.snake.body:
            self.grid[seg.position.x][seg.position.y] = seg
        self.grid[self.food.position.x][self.food.position.y] = self.food
    
    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                if cell !=None:
                    self.game_window.blit(cell.image, (cell.position.x*Constants.PIXEL_SIZE[0], cell.position.y*Constants.PIXEL_SIZE[1]))

            

if __name__ == '__main__':
    Game()