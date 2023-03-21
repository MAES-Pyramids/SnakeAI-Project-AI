import random
from util.constants import CONSTANTS


class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> None:
        return self._x

    @x.setter
    def x(self, new_x) -> None:
        self._x = new_x

    @property
    def y(self, ) -> None:
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @staticmethod
    def get_random_point() -> 'Point':
        return Point(
            random.randint(2, CONSTANTS.GRID_SIZE[0]-2),
            random.randint(2, CONSTANTS.GRID_SIZE[1]-2),
        )

    def __add__(self, other: 'Point') -> 'Point':
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __mul__(self, val: 'Point') -> 'Point':
        return Point(
            self.x * val,
            self.y * val
        )

    def __eq__(self, other: 'Point') -> bool:
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self) -> str:
        return f"{self.x} : {self.y}"

    def __repr__(self) -> str:
        return f"{self.x} : {self.y}"
    
    def __hash__(self):
        return hash((self.x, self.y))
