class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    

    def setX(self, x):
        self.x = x
        self.position[0] = x
    
    def setY(self, y):
        self.y = y
        self.position[1] = y


    def  __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
    
    def  __mul__(self, val):
        return Point(
            self.x *val,
            self.y *val
        )
    
    def __eq__(self, other):
        return self.position == other.position

    def __str__(self) -> str:
        return f"{self.x} : {self.y}"



