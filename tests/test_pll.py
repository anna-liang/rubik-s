import unittest
import algorithms.pll as pll_algorithms
from model.cube import Colour, Cube

class TestPLL(unittest.TestCase):
    def setUp(self):
        self.expected_faces = [
            [Colour.WHITE] * 9, 
            [Colour.RED] * 9, 
            [Colour.GREEN] * 9, 
            [Colour.ORANGE] * 9, 
            [Colour.BLUE] * 9,
            [Colour.YELLOW] * 9
        ]
         
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
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL diagonal corner swap.")

    def test_vertical_corner_swap(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] * 2 + [Colour.BLUE] + [Colour.RED] * 6,
            [Colour.GREEN] + [Colour.BLUE] + [Colour.GREEN] * 7, 
            [Colour.BLUE] + [Colour.ORANGE] * 8,
            [Colour.ORANGE] + [Colour.GREEN] + [Colour.RED] + [Colour.BLUE] * 6, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL vertical corner swap.")

    def test_triangle_ccw(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] + [Colour.BLUE] + [Colour.RED] * 7,
            [Colour.GREEN] + [Colour.RED] + [Colour.GREEN] * 7, 
            [Colour.ORANGE] * 9,
            [Colour.BLUE] + [Colour.GREEN] + [Colour.BLUE] * 7, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL triangle CCW.")

    def test_triangle_cw(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] + [Colour.GREEN] + [Colour.RED] * 7,
            [Colour.GREEN] + [Colour.BLUE] + [Colour.GREEN] * 7, 
            [Colour.ORANGE] * 9,
            [Colour.BLUE] + [Colour.RED] + [Colour.BLUE] * 7, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL triangle CW.")

    def test_cross_swap(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] + [Colour.ORANGE] + [Colour.RED] * 7,
            [Colour.GREEN] + [Colour.BLUE] + [Colour.GREEN] * 7, 
            [Colour.ORANGE] + [Colour.RED] + [Colour.ORANGE] * 7,
            [Colour.BLUE] + [Colour.GREEN] + [Colour.BLUE] * 7, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL cross swap.")

    def test_diagonal_edge_swap(self):
        initial_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED] + [Colour.BLUE] + [Colour.RED] * 7,
            [Colour.GREEN] + [Colour.ORANGE] + [Colour.GREEN] * 7, 
            [Colour.ORANGE] + [Colour.GREEN] + [Colour.ORANGE] * 7,
            [Colour.BLUE] + [Colour.RED] + [Colour.BLUE] * 7, 
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        pll_algorithms.pll(initial_cube)
        self.assertEqual(initial_cube.faces, self.expected_faces, f"Wrong after PLL diagonal edge swap.")

if __name__ == '__main__':
    unittest.main()
