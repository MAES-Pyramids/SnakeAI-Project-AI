from util.point import Point
from util.constants import CONSTANTS
from sprites.game_object import GameObject
import pygame


class Food(GameObject):
    def __init__(self,
                 position=Point(0, 0),
                 image=pygame.Surface([CONSTANTS.PIXEL_SIZE]*2)) -> None:
        super().__init__(position, image)
        self.image.fill("#FFC947")
        self.spawn()

    def spawn(self, obstacles = [], snake = []) -> None:
        self.position = Point.get_random_point()
        for obstacle in obstacles:
            if self.position == obstacle.position:
                self.spawn(obstacles=obstacles)
        for brick in snake:
            if self.position == brick.position:
                self.spawn(obstacles=obstacles, snake=snake)
        self.update_rect()
