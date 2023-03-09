import sys
sys.path.append('util')
from point import Point
from util.point import Point


class Direction:
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    RIGHT = Point(1, 0)
    LEFT = Point(-1, 0)

    def __eq__(self, other: object) -> bool:
        return self == other
