import unittest
import check
from model.cube import Colour, Cube

class TestAlgorithms(unittest.TestCase):
    def test_is_cube_solved_solved_cube(self):
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
    def test_is_cube_solved_unsolved_cube(self):
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
    # def test_is_cube_solved_illegal_layout(self):
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
