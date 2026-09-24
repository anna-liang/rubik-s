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
        return f"TOP: \n{self.faces[0][0:3]}\n{self.faces[0][3:6]}\n{self.faces[0][6:9]}\nFRONT: \n{self.faces[1][0:3]}\n{self.faces[1][3:6]}\n{self.faces[1][6:9]}\nLEFT: \n{self.faces[2][0:3]}\n{self.faces[2][3:6]}\n{self.faces[2][6:9]}\nBACK: \n{self.faces[3][0:3]}\n{self.faces[3][3:6]}\n{self.faces[3][6:9]}\nRIGHT: \n{self.faces[4][0:3]}\n{self.faces[4][3:6]}\n{self.faces[4][6:9]}\nBOTTOM: \n{self.faces[5][0:3]}\n{self.faces[5][3:6]}\n{self.faces[5][6:9]}"
    
