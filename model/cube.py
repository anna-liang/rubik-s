from enum import Enum

class Colour(Enum):
    WHITE = 0
    YELLOW = 1
    RED = 2
    ORANGE = 3
    BLUE = 4
    GREEN = 5

class Piece:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Corner(Piece):
    def __init__(self, left, right, top):
        super().__init__(left, right)
        self.top = top

class Side(Piece):
    def __init__(self, left, right):
        super().__init__(left, right)

class Top:
    def __init__(self, pieces: list[Piece]):
        self.pieces = pieces

class Middle:
    def __init__(self, pieces: list[Piece]):
        self.pieces = pieces

class Bottom:
    def __init__(self, pieces: list[Piece]):
        self.pieces = pieces

class Cube:
    def __init__(self, top: Top, middle: Middle, bottom: Bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
