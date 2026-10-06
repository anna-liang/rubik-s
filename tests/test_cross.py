import unittest
import algorithms.cross as cross_algorithms
from model.cube import Colour, Cube
from constants.algorithm import Moves

class TestAlgorithmsCross(unittest.TestCase):
    def test_cross_top_face_top(self):
        initial_cube = Cube([
            [
                Colour.BLUE, Colour.YELLOW, Colour.RED,
                Colour.BLUE, Colour.WHITE, Colour.GREEN,
                Colour.RED, Colour.RED, Colour.GREEN
            ],
            [
                Colour.BLUE, Colour.GREEN, Colour.YELLOW,
                Colour.ORANGE, Colour.RED, Colour.BLUE,
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.YELLOW,
                Colour.WHITE, Colour.GREEN, Colour.GREEN,
                Colour.YELLOW, Colour.RED, Colour.BLUE
            ],
            [
                Colour.GREEN, Colour.GREEN, Colour.ORANGE,
                Colour.ORANGE, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.GREEN
            ],
            [
                Colour.RED, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.YELLOW, Colour.GREEN,
                Colour.WHITE, Colour.YELLOW, Colour.YELLOW,
                Colour.ORANGE, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.YELLOW, Colour.GREEN, Colour.GREEN,
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.ORANGE, Colour.BLUE, Colour.RED
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.ORANGE, Colour.RED, Colour.BLUE,
                Colour.WHITE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.BLUE, Colour.RED, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN
            ],
            [
                Colour.RED, Colour.WHITE, Colour.ORANGE,
                Colour.ORANGE, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.BLUE, Colour.GREEN, Colour.YELLOW,
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.RED, Colour.YELLOW, Colour.GREEN,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after top face top edge.")

    def test_cross_top_face_right(self):
        initial_cube = Cube([
            [
                Colour.WHITE, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.GREEN, Colour.BLUE
            ],
            [
                Colour.GREEN, Colour.RED, Colour.RED,
                Colour.WHITE, Colour.RED, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.YELLOW,
            ],
            [
                Colour.GREEN, Colour.RED, Colour.RED,
                Colour.GREEN, Colour.GREEN, Colour.BLUE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE
            ],
            [
                Colour.GREEN, Colour.BLUE, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.YELLOW, Colour.RED, Colour.WHITE,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.ORANGE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
                Colour.GREEN, Colour.WHITE, Colour.ORANGE,
                Colour.ORANGE, Colour.WHITE, Colour.YELLOW
            ],
            [
                Colour.YELLOW, Colour.ORANGE, Colour.GREEN,
                Colour.RED, Colour.RED, Colour.WHITE,
                Colour.WHITE, Colour.RED, Colour.YELLOW,
            ],
            [
                Colour.GREEN, Colour.RED, Colour.BLUE,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN
            ],
            [
                Colour.GREEN, Colour.RED, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.ORANGE, Colour.BLUE, Colour.ORANGE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
                Colour.RED, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.RED, Colour.YELLOW, Colour.BLUE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after top face right edge.")

    def test_cross_top_face_bottom(self):
        initial_cube = Cube([
            [
                Colour.ORANGE, Colour.GREEN, Colour.BLUE,
                Colour.BLUE, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.YELLOW, Colour.WHITE
            ],
            [
                Colour.WHITE, Colour.BLUE, Colour.GREEN,
                Colour.ORANGE, Colour.RED, Colour.BLUE,
                Colour.WHITE, Colour.RED, Colour.GREEN,
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.BLUE,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.YELLOW,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.RED, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.RED, Colour.RED, Colour.YELLOW,
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.YELLOW,
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.BLUE,
                Colour.BLUE, Colour.YELLOW, Colour.BLUE
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.BLUE, Colour.WHITE, Colour.YELLOW,
                Colour.GREEN, Colour.WHITE, Colour.BLUE,
                Colour.ORANGE, Colour.BLUE, Colour.BLUE
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.RED,
                Colour.ORANGE, Colour.RED, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.RED,
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE
            ],
            [
                Colour.GREEN, Colour.RED, Colour.YELLOW,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.YELLOW, Colour.RED, Colour.RED,
                Colour.WHITE, Colour.BLUE, Colour.ORANGE,
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after top face bottom edge.")

    def test_cross_top_face_left(self):
        initial_cube = Cube([
            [
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.YELLOW, Colour.WHITE, Colour.GREEN,
                Colour.WHITE, Colour.WHITE, Colour.GREEN
            ],
            [
                Colour.RED, Colour.RED, Colour.ORANGE,
                Colour.ORANGE, Colour.RED, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.BLUE,
            ],
            [
                Colour.WHITE, Colour.BLUE, Colour.GREEN,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE
            ],
            [
                Colour.BLUE, Colour.WHITE, Colour.BLUE,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE,
                Colour.YELLOW, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.YELLOW,
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.ORANGE, Colour.ORANGE, Colour.RED,
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.BLUE,
                Colour.BLUE, Colour.YELLOW, Colour.GREEN
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.GREEN, Colour.WHITE, Colour.BLUE,
                Colour.RED, Colour.BLUE, Colour.GREEN
            ],
            [
                Colour.BLUE, Colour.WHITE, Colour.YELLOW,
                Colour.ORANGE, Colour.RED, Colour.BLUE,
                Colour.WHITE, Colour.RED, Colour.RED,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE
            ],
            [
                Colour.BLUE, Colour.RED, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.RED, Colour.ORANGE, Colour.ORANGE,
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after top face left edge.")

    def test_cross_front_face_top(self):
        initial_cube = Cube([
            [
                Colour.YELLOW, Colour.BLUE, Colour.GREEN,
                Colour.WHITE, Colour.WHITE, Colour.BLUE,
                Colour.RED, Colour.RED, Colour.ORANGE
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.YELLOW,
                Colour.GREEN, Colour.RED, Colour.BLUE,
                Colour.GREEN, Colour.ORANGE, Colour.WHITE,
            ],
            [
                Colour.BLUE, Colour.RED, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.RED
            ],
            [
                Colour.RED, Colour.ORANGE, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.ORANGE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.GREEN, Colour.GREEN, Colour.GREEN,
                Colour.BLUE, Colour.WHITE, Colour.BLUE,
                Colour.ORANGE, Colour.WHITE, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.BLUE,
                Colour.BLUE, Colour.RED, Colour.RED,
                Colour.RED, Colour.RED, Colour.RED,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.GREEN,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.YELLOW, Colour.ORANGE, Colour.ORANGE,
                Colour.WHITE, Colour.BLUE, Colour.RED,
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after front face top edge.")

    def test_cross_front_face_right(self):
        initial_cube = Cube([
            [
                Colour.GREEN, Colour.GREEN, Colour.GREEN,
                Colour.BLUE, Colour.WHITE, Colour.BLUE,
                Colour.YELLOW, Colour.WHITE, Colour.ORANGE
            ],
            [
                Colour.BLUE, Colour.RED, Colour.GREEN,
                Colour.BLUE, Colour.RED, Colour.YELLOW,
                Colour.RED, Colour.RED, Colour.RED,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.ORANGE,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.YELLOW, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.BLUE, Colour.RED,
                Colour.WHITE, Colour.WHITE, Colour.RED,
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.BLUE,
                Colour.YELLOW, Colour.YELLOW, Colour.ORANGE,
                Colour.BLUE, Colour.YELLOW, Colour.GREEN
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.WHITE, Colour.ORANGE,
                Colour.YELLOW, Colour.WHITE, Colour.GREEN
            ],
            [
                Colour.BLUE, Colour.RED, Colour.YELLOW,
                Colour.BLUE, Colour.RED, Colour.GREEN,
                Colour.RED, Colour.RED, Colour.RED,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.ORANGE,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.RED, Colour.WHITE, Colour.ORANGE,
                Colour.RED, Colour.BLUE, Colour.WHITE,
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.WHITE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after front face right edge.")

    def test_cross_front_face_bottom(self):
        initial_cube = Cube([
            [
                Colour.ORANGE, Colour.RED, Colour.BLUE,
                Colour.WHITE, Colour.WHITE, Colour.BLUE,
                Colour.ORANGE, Colour.RED, Colour.GREEN
            ],
            [
                Colour.GREEN, Colour.BLUE, Colour.YELLOW,
                Colour.BLUE, Colour.RED, Colour.GREEN,
                Colour.WHITE, Colour.YELLOW, Colour.ORANGE,
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.GREEN,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.RED, Colour.ORANGE, Colour.RED,
                Colour.RED, Colour.BLUE, Colour.WHITE,
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.RED, Colour.RED, Colour.BLUE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.ORANGE, Colour.BLUE, Colour.YELLOW,
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.RED
            ],
            [
                Colour.YELLOW, Colour.GREEN, Colour.WHITE,
                Colour.BLUE, Colour.RED, Colour.RED,
                Colour.BLUE, Colour.RED, Colour.BLUE,
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.GREEN,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.ORANGE, Colour.ORANGE, Colour.GREEN,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.GREEN, Colour.BLUE, Colour.GREEN,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.ORANGE, Colour.YELLOW, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after front face bottom edge.")

    def test_cross_front_face_left(self):
        initial_cube = Cube([
            [
                Colour.BLUE, Colour.BLUE, Colour.GREEN,
                Colour.RED, Colour.WHITE, Colour.BLUE,
                Colour.GREEN, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.ORANGE,
                Colour.YELLOW, Colour.RED, Colour.BLUE,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.RED,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.BLUE
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.RED, Colour.BLUE, Colour.WHITE,
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.RED, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
                Colour.RED, Colour.WHITE, Colour.ORANGE,
                Colour.RED, Colour.RED, Colour.RED
            ],
            [
                Colour.YELLOW, Colour.GREEN, Colour.WHITE,
                Colour.BLUE, Colour.RED, Colour.BLUE,
                Colour.BLUE, Colour.RED, Colour.GREEN,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.GREEN,
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.BLUE, Colour.ORANGE, Colour.WHITE
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.ORANGE,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.ORANGE, Colour.YELLOW, Colour.ORANGE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after front face left edge.")

    def test_cross_left_face_top(self):
        initial_cube = Cube([
            [
                Colour.BLUE, Colour.WHITE, Colour.ORANGE,
                Colour.RED, Colour.WHITE, Colour.RED,
                Colour.RED, Colour.RED, Colour.BLUE
            ],
            [
                Colour.YELLOW, Colour.GREEN, Colour.ORANGE,
                Colour.ORANGE, Colour.RED, Colour.GREEN,
                Colour.GREEN, Colour.BLUE, Colour.RED,
            ],
            [
                Colour.ORANGE, Colour.YELLOW, Colour.GREEN,
                Colour.BLUE, Colour.GREEN, Colour.BLUE,
                Colour.GREEN, Colour.GREEN, Colour.RED
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.YELLOW,
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.GREEN,
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.GREEN, Colour.BLUE, Colour.YELLOW,
                Colour.RED, Colour.WHITE, Colour.RED,
                Colour.YELLOW, Colour.WHITE, Colour.WHITE
            ],
            [
                Colour.RED, Colour.BLUE, Colour.GREEN,
                Colour.GREEN, Colour.RED, Colour.ORANGE,
                Colour.BLUE, Colour.RED, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.GREEN, Colour.BLUE,
                Colour.ORANGE, Colour.GREEN, Colour.ORANGE,
                Colour.WHITE, Colour.GREEN, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.RED, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.WHITE,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.RED, Colour.WHITE, Colour.RED,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.ORANGE, Colour.YELLOW, Colour.BLUE,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.GREEN, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after left face top edge.")

    def test_cross_left_face_right(self):
        initial_cube = Cube([
            [
                Colour.ORANGE, Colour.ORANGE, Colour.ORANGE,
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.RED, Colour.RED, Colour.BLUE
            ],
            [
                Colour.GREEN, Colour.GREEN, Colour.ORANGE,
                Colour.RED, Colour.RED, Colour.GREEN,
                Colour.RED, Colour.BLUE, Colour.RED,
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.WHITE,
                Colour.BLUE, Colour.GREEN, Colour.YELLOW,
                Colour.GREEN, Colour.GREEN, Colour.GREEN
            ],
            [
                Colour.YELLOW, Colour.BLUE, Colour.GREEN,
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.BLUE,
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.ORANGE, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.YELLOW, Colour.WHITE, Colour.GREEN
            ],
            [
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.GREEN, Colour.RED, Colour.WHITE,
                Colour.ORANGE, Colour.RED, Colour.RED,
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.BLUE,
                Colour.BLUE, Colour.GREEN, Colour.ORANGE,
                Colour.GREEN, Colour.GREEN, Colour.BLUE
            ],
            [
                Colour.WHITE, Colour.BLUE, Colour.GREEN,
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.GREEN, Colour.ORANGE,
                Colour.RED, Colour.BLUE, Colour.WHITE,
                Colour.YELLOW, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.YELLOW, Colour.YELLOW, Colour.GREEN,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after left face right edge.")
    
    def test_cross_left_face_left(self):
        initial_cube = Cube([
            [
                Colour.YELLOW, Colour.WHITE, Colour.WHITE,
                Colour.RED, Colour.WHITE, Colour.WHITE,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.BLUE, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.GREEN,
                Colour.RED, Colour.BLUE, Colour.RED,
            ],
            [
                Colour.GREEN, Colour.GREEN, Colour.ORANGE,
                Colour.YELLOW, Colour.GREEN, Colour.RED,
                Colour.YELLOW, Colour.GREEN, Colour.WHITE
            ],
            [
                Colour.BLUE, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.ORANGE, Colour.RED,
                Colour.ORANGE, Colour.RED, Colour.ORANGE
            ],
            [
                Colour.WHITE, Colour.ORANGE, Colour.RED,
                Colour.ORANGE, Colour.BLUE, Colour.YELLOW,
                Colour.BLUE, Colour.BLUE, Colour.YELLOW,
            ],
            [
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.BLUE, Colour.BLUE, Colour.GREEN
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.WHITE, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.WHITE, Colour.RED,
                Colour.YELLOW, Colour.WHITE, Colour.GREEN
            ],
            [
                Colour.RED, Colour.BLUE, Colour.RED,
                Colour.GREEN, Colour.RED, Colour.WHITE,
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.BLUE, Colour.GREEN, Colour.BLUE,
                Colour.WHITE, Colour.GREEN, Colour.ORANGE,
                Colour.GREEN, Colour.GREEN, Colour.BLUE
            ],
            [
                Colour.WHITE, Colour.BLUE, Colour.RED,
                Colour.ORANGE, Colour.ORANGE, Colour.ORANGE,
                Colour.ORANGE, Colour.RED, Colour.YELLOW
            ],
            [
                Colour.WHITE, Colour.GREEN, Colour.ORANGE,
                Colour.RED, Colour.BLUE, Colour.YELLOW,
                Colour.WHITE, Colour.BLUE, Colour.YELLOW,
            ],
            [
                Colour.YELLOW, Colour.YELLOW, Colour.GREEN,
                Colour.YELLOW, Colour.YELLOW, Colour.YELLOW,
                Colour.RED, Colour.BLUE, Colour.GREEN
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after left face left edge.")

    def test_cross_left_face_bottom(self):
        initial_cube = Cube([
            [
                Colour.GREEN, Colour.GREEN, Colour.RED,
                Colour.ORANGE, Colour.WHITE, Colour.BLUE,
                Colour.YELLOW, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
                Colour.GREEN, Colour.RED, Colour.GREEN,
                Colour.YELLOW, Colour.BLUE, Colour.RED,
            ],
            [
                Colour.ORANGE, Colour.WHITE, Colour.RED,
                Colour.WHITE, Colour.GREEN, Colour.RED,
                Colour.GREEN, Colour.YELLOW, Colour.ORANGE
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.BLUE, Colour.RED, Colour.WHITE,
                Colour.ORANGE, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.BLUE, Colour.WHITE, Colour.YELLOW,
                Colour.RED, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.RED
            ]
        ])
        cross_algorithms.cross(initial_cube)
        expected_faces = [
            [
                Colour.RED, Colour.ORANGE, Colour.WHITE,
                Colour.GREEN, Colour.WHITE, Colour.RED,
                Colour.YELLOW, Colour.WHITE, Colour.GREEN
            ],
            [
                Colour.RED, Colour.BLUE, Colour.YELLOW,
                Colour.GREEN, Colour.RED, Colour.ORANGE,
                Colour.BLUE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.GREEN, Colour.YELLOW, Colour.BLUE,
                Colour.BLUE, Colour.GREEN, Colour.ORANGE,
                Colour.GREEN, Colour.RED, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.BLUE, Colour.WHITE,
                Colour.GREEN, Colour.ORANGE, Colour.RED,
                Colour.BLUE, Colour.ORANGE, Colour.ORANGE
            ],
            [
                Colour.RED, Colour.WHITE, Colour.ORANGE,
                Colour.WHITE, Colour.BLUE, Colour.WHITE,
                Colour.BLUE, Colour.BLUE, Colour.WHITE,
            ],
            [
                Colour.ORANGE, Colour.YELLOW, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.YELLOW,
                Colour.YELLOW, Colour.YELLOW, Colour.RED
            ]
        ]
        self.assertEqual(initial_cube.faces, expected_faces, f"Wrong after left face bottom edge.")

if __name__ == '__main__':
    unittest.main()
