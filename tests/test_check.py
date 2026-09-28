import unittest
import check
from model.cube import Colour, Cube

class TestAlgorithms(unittest.TestCase):
    def test_cross_complete(self):
        cube = Cube([
            [
                Colour.ORANGE, Colour.RED, Colour.RED,
                Colour.BLUE, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.WHITE, Colour.WHITE
            ],
            [
                Colour.YELLOW, Colour.BLUE, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.ORANGE,
                Colour.RED, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.BLUE, Colour.ORANGE, Colour.GREEN,
                Colour.RED, Colour.GREEN, Colour.ORANGE,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.WHITE, Colour.GREEN, Colour.WHITE,
                Colour.WHITE, Colour.ORANGE, Colour.BLUE,
                Colour.BLUE, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.RED, Colour.GREEN, Colour.BLUE,
                Colour.GREEN, Colour.BLUE, Colour.RED,
                Colour.WHITE, Colour.BLUE, Colour.YELLOW,
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.GREEN, Colour.YELLOW, Colour.ORANGE
            ]
        ])
        self.assertTrue(check.is_cross_complete(cube))

    def test_cross_not_complete(self):
        cube = Cube([
            [
                Colour.ORANGE, Colour.RED, Colour.RED,
                Colour.BLUE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.BLUE
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.RED,
                Colour.ORANGE, Colour.RED, Colour.WHITE,
                Colour.GREEN, Colour.BLUE, Colour.YELLOW,
            ],
            [
                Colour.BLUE, Colour.ORANGE, Colour.WHITE,
                Colour.RED, Colour.GREEN, Colour.GREEN,
                Colour.ORANGE, Colour.GREEN, Colour.RED
            ],
            [
                Colour.WHITE, Colour.GREEN, Colour.WHITE,
                Colour.WHITE, Colour.ORANGE, Colour.BLUE,
                Colour.BLUE, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.YELLOW, Colour.GREEN, Colour.BLUE,
                Colour.ORANGE, Colour.BLUE, Colour.RED,
                Colour.GREEN, Colour.BLUE, Colour.YELLOW,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.GREEN, Colour.YELLOW, Colour.ORANGE
            ]
        ])
        self.assertFalse(check.is_cross_complete(cube))

    def test_solved_cube(self):
        cube = Cube([
            [Colour.BLUE] * 9, 
            [Colour.YELLOW] * 9, 
            [Colour.RED] * 9, 
            [Colour.WHITE] * 9, 
            [Colour.ORANGE] * 9,
            [Colour.GREEN] * 9
        ])
        self.assertTrue(check.is_cube_solved(cube))
    
    # missing GREEN
    def test_unsolved_cube(self):
        cube = Cube([
            [Colour.BLUE] * 9, 
            [Colour.YELLOW] * 9, 
            [Colour.RED] * 9, 
            [Colour.WHITE] * 9, 
            [Colour.ORANGE] * 9,
            [Colour.BLUE] * 9
        ])
        self.assertFalse(check.is_cube_solved(cube))

    # TODO: need to implement
    # def test_solved_illegal_layout(self):
    #     cube = Cube([
    #         [Colour.ORANGE] * 9, 
    #         [Colour.YELLOW] * 9, 
    #         [Colour.RED] * 9, 
    #         [Colour.WHITE] * 9, 
    #         [Colour.BLUE] * 9,
    #         [[Colour.GREEN] * 9]
    #     ])
    #     self.assertFalse(check.is_cube_solved(cube))

if __name__ == '__main__':
    unittest.main()
