import unittest
import algorithms.oll as oll_algorithms
from model.cube import Colour, Cube

class TestPLL(unittest.TestCase):
    def test_dot(self):
        initial_faces = [
            [
                Colour.GREEN, Colour.RED, Colour.ORANGE,
                Colour.ORANGE, Colour.WHITE, Colour.BLUE,
                Colour.RED, Colour.GREEN, Colour.GREEN,
            ],
            [Colour.WHITE, Colour.WHITE, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.WHITE, Colour.WHITE, Colour.BLUE] + [Colour.GREEN] * 6,
            [Colour.BLUE, Colour.WHITE, Colour.RED] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.WHITE, Colour.WHITE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
                Colour.ORANGE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.WHITE, Colour.BLUE,
            ],
            [Colour.ORANGE, Colour.RED, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.BLUE, Colour.WHITE, Colour.WHITE] + [Colour.GREEN] * 6,
            [Colour.RED, Colour.WHITE, Colour.WHITE] + [Colour.ORANGE] * 6,
            [Colour.RED, Colour.GREEN, Colour.GREEN] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL dot.")

    def test_l(self):
        initial_faces = [
            [
                Colour.WHITE, Colour.GREEN, Colour.RED,
                Colour.BLUE, Colour.WHITE, Colour.WHITE,
                Colour.BLUE, Colour.WHITE, Colour.GREEN,
            ],
            [Colour.WHITE, Colour.RED, Colour.RED] + [Colour.RED] * 6,
            [Colour.GREEN, Colour.WHITE, Colour.ORANGE] + [Colour.GREEN] * 6,
            [Colour.WHITE, Colour.WHITE, Colour.ORANGE] + [Colour.ORANGE] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.BLUE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [
                Colour.RED, Colour.WHITE, Colour.GREEN,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.WHITE, Colour.ORANGE,
            ],
            [Colour.WHITE, Colour.GREEN, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.WHITE, Colour.RED, Colour.RED] + [Colour.GREEN] * 6,
            [Colour.ORANGE, Colour.BLUE, Colour.BLUE] + [Colour.ORANGE] * 6,
            [Colour.BLUE, Colour.ORANGE, Colour.WHITE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL L.")

    def test_line(self):
        initial_faces = [
            [
                Colour.BLUE, Colour.RED, Colour.WHITE,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.WHITE, Colour.BLUE, Colour.BLUE,
            ],
            [Colour.RED, Colour.WHITE, Colour.ORANGE] + [Colour.RED] * 6,
            [Colour.RED, Colour.GREEN, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.WHITE, Colour.WHITE] + [Colour.ORANGE] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.ORANGE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.BLUE, Colour.WHITE, Colour.GREEN,
            ],
            [Colour.WHITE, Colour.RED, Colour.RED] + [Colour.RED] * 6,
            [Colour.GREEN, Colour.GREEN, Colour.ORANGE] + [Colour.GREEN] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.ORANGE] + [Colour.ORANGE] * 6,
            [Colour.WHITE, Colour.BLUE, Colour.BLUE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL line.")

    def test_t(self):
        initial_faces = [
            [
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.WHITE, Colour.GREEN,
            ],
            [Colour.WHITE, Colour.GREEN, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.RED, Colour.RED, Colour.BLUE] + [Colour.GREEN] * 6,
            [Colour.ORANGE, Colour.BLUE, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.ORANGE, Colour.BLUE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.GREEN, Colour.GREEN, Colour.BLUE] + [Colour.RED] * 6,
            [Colour.RED, Colour.RED, Colour.ORANGE] + [Colour.GREEN] * 6,
            [Colour.BLUE, Colour.BLUE, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.ORANGE, Colour.RED] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL T.")

    def test_right_corners(self):
        initial_faces = [
            [
                Colour.WHITE, Colour.WHITE, Colour.ORANGE,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.WHITE, Colour.WHITE, Colour.BLUE,
            ],
            [Colour.RED, Colour.ORANGE, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.ORANGE, Colour.RED, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.WHITE, Colour.BLUE, Colour.BLUE] + [Colour.ORANGE] * 6,
            [Colour.RED, Colour.GREEN, Colour.GREEN] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.RED, Colour.ORANGE, Colour.ORANGE] + [Colour.RED] * 6,
            [Colour.BLUE, Colour.RED, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.ORANGE, Colour.BLUE, Colour.RED] + [Colour.ORANGE] * 6,
            [Colour.GREEN, Colour.GREEN, Colour.BLUE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL right corners.")

    def test_diagonal_corners(self):
        initial_faces = [
            [
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.ORANGE, Colour.WHITE, Colour.WHITE,
            ],
            [Colour.WHITE, Colour.BLUE, Colour.BLUE] + [Colour.RED] * 6,
            [Colour.BLUE, Colour.GREEN, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.ORANGE, Colour.RED] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.RED, Colour.WHITE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.BLUE] * 3 + [Colour.RED] * 6,
            [Colour.RED, Colour.GREEN, Colour.RED] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.ORANGE, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.RED, Colour.ORANGE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL diagonal corners.")

    def test_bottom_left_fish(self):
        initial_faces = [
            [
                Colour.ORANGE, Colour.WHITE, Colour.BLUE,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.WHITE, Colour.WHITE, Colour.RED,
            ],
            [Colour.GREEN, Colour.BLUE, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.BLUE, Colour.RED, Colour.ORANGE] + [Colour.GREEN] * 6,
            [Colour.RED, Colour.GREEN, Colour.WHITE] + [Colour.ORANGE] * 6,
            [Colour.GREEN, Colour.ORANGE, Colour.WHITE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.BLUE] * 3 + [Colour.RED] * 6,
            [Colour.RED, Colour.GREEN, Colour.RED] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.ORANGE, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.RED, Colour.ORANGE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL bottom left fish.")

    def test_top_right_fish(self):
        initial_faces = [
            [
                Colour.BLUE, Colour.WHITE, Colour.WHITE,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.ORANGE, Colour.WHITE, Colour.GREEN,
            ],
            [Colour.WHITE, Colour.BLUE, Colour.RED] + [Colour.RED] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.BLUE, Colour.RED, Colour.ORANGE] + [Colour.ORANGE] * 6,
            [Colour.WHITE, Colour.GREEN, Colour.RED] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.BLUE] * 3 + [Colour.RED] * 6,
            [Colour.RED, Colour.GREEN, Colour.RED] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.ORANGE, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.RED, Colour.ORANGE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL top right fish.")

    def test_car(self):
        initial_faces = [
            [
                Colour.BLUE, Colour.WHITE, Colour.RED,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.WHITE, Colour.RED,
            ],
            [Colour.ORANGE, Colour.RED, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.WHITE, Colour.BLUE, Colour.WHITE] + [Colour.GREEN] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.ORANGE] + [Colour.ORANGE] * 6,
            [Colour.GREEN, Colour.GREEN, Colour.BLUE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.BLUE] * 3 + [Colour.RED] * 6,
            [Colour.RED, Colour.ORANGE, Colour.RED] + [Colour.GREEN] * 6,
            [Colour.GREEN, Colour.RED, Colour.GREEN] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.GREEN, Colour.ORANGE] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL car.")

    def test_h(self):
        initial_faces = [
            [
                Colour.BLUE, Colour.WHITE, Colour.GREEN,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.ORANGE, Colour.WHITE, Colour.ORANGE,
            ],
            [Colour.WHITE, Colour.RED, Colour.WHITE] + [Colour.RED] * 6,
            [Colour.RED, Colour.BLUE, Colour.GREEN] + [Colour.GREEN] * 6,
            [Colour.WHITE, Colour.ORANGE, Colour.WHITE] + [Colour.ORANGE] * 6,
            [Colour.BLUE, Colour.GREEN, Colour.RED] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        expected_faces = [
            [Colour.WHITE] * 9,
            [Colour.GREEN, Colour.RED, Colour.BLUE] + [Colour.RED] * 6,
            [Colour.BLUE, Colour.ORANGE, Colour.ORANGE] + [Colour.GREEN] * 6,
            [Colour.RED, Colour.GREEN, Colour.RED] + [Colour.ORANGE] * 6,
            [Colour.ORANGE, Colour.BLUE, Colour.GREEN] + [Colour.BLUE] * 6,
            [Colour.YELLOW] * 9
        ]
        initial_cube = Cube(initial_faces)
        oll_algorithms.oll(initial_cube)
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after OLL H.")

if __name__ == '__main__':
    unittest.main()
