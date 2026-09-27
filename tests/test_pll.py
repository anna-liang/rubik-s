import unittest
import algorithms.pll as pll_algorithms
from model.cube import Colour, Cube

class TestPLL(unittest.TestCase):
    def test_diagonal_corner_swap(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] * 2 + [Colour.ORANGE] + [Colour.RED] * 6, 
            [Colour.BLUE] + [Colour.ORANGE] + [Colour.GREEN] * 7, 
            [Colour.ORANGE] + [Colour.GREEN] + [Colour.RED] + [Colour.ORANGE] * 6,
            [Colour.GREEN] + [Colour.BLUE] * 8, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        expected_faces = [
            [Colour.WHITE] * 9, 
            [Colour.RED] * 9, 
            [Colour.GREEN] * 9, 
            [Colour.ORANGE] * 9, 
            [Colour.BLUE] * 9,
            [Colour.YELLOW] * 9
        ]
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after PLL diagonal corner swap.")

if __name__ == '__main__':
    unittest.main()
