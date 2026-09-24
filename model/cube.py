from enum import Enum

class Colour(Enum):
    WHITE = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
    YELLOW = 5

class Cube:
    def __init__(self, cube):
        self.faces = cube

    def __str__(self):
        return f"{self.faces}"
    
