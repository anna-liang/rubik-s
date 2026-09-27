import unittest
import algorithms.algorithms as algorithms
from model.cube import Colour, Cube
from constants.algorithm import Moves

class TestAlgorithmsScrambled(unittest.TestCase):
    def setUp(self):
        # Scramble Algo: L' B R' B2 L2 D B U R B2 L F2 U2 R' B2 R' F2 R B2 L' B' L
        self.initial_cube = Cube([
            [
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN,
                Colour.YELLOW, Colour.BLUE, Colour.YELLOW
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.BLUE
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
                Colour.ORANGE, Colour.BLUE, Colour.RED,
                Colour.BLUE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.RED, Colour.GREEN, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.GREEN
            ]
        ])

    def test_apply_move_4_times(self):
        expected_faces = [
            [
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.WHITE, Colour.RED, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN,
                Colour.YELLOW, Colour.BLUE, Colour.YELLOW
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.GREEN, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.BLUE
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
                Colour.ORANGE, Colour.BLUE, Colour.RED,
                Colour.BLUE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.RED, Colour.GREEN, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.GREEN
            ]
        ]
        for move in Moves:
            algorithms.apply_move(self.initial_cube, move)
            algorithms.apply_move(self.initial_cube, move)
            algorithms.apply_move(self.initial_cube, move)
            algorithms.apply_move(self.initial_cube, move)
            
            self.assertEqual(self.initial_cube.faces, expected_faces, f"Applying {move} 4 times does not revert to original")

    def test_apply_U_move(self):
        algorithms.apply_move(self.initial_cube, Moves.U)
        expected_faces_after_U = [
            [
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
                Colour.WHITE, Colour.RED, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN,
                Colour.YELLOW, Colour.BLUE, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.BLUE
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.ORANGE, Colour.BLUE, Colour.RED,
                Colour.BLUE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.RED, Colour.GREEN, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.GREEN
            ]
        ]
        self.assertEqual(self.initial_cube.faces, expected_faces_after_U, "The faces are incorrect for U move")

    def test_apply_U_prime_move(self):
        algorithms.apply_move(self.initial_cube, Moves.U_PRIME)
        expected_faces_after_U_prime = [
            [
                Colour.RED, Colour.BLUE, Colour.BLUE,
                Colour.GREEN, Colour.WHITE, Colour.YELLOW,
                Colour.YELLOW, Colour.ORANGE, Colour.YELLOW
            ],
            [
                Colour.GREEN, Colour.ORANGE, Colour.ORANGE,
                Colour.WHITE, Colour.RED, Colour.WHITE,
                Colour.GREEN, Colour.YELLOW, Colour.WHITE,
            ],
            [
                Colour.WHITE, Colour.WHITE, Colour.WHITE,
                Colour.ORANGE, Colour.GREEN, Colour.GREEN,
                Colour.YELLOW, Colour.BLUE, Colour.YELLOW
            ],
            [
                Colour.ORANGE, Colour.RED, Colour.ORANGE,
                Colour.GREEN, Colour.ORANGE, Colour.BLUE,
                Colour.WHITE, Colour.BLUE, Colour.BLUE
            ],
            [
                Colour.BLUE, Colour.YELLOW, Colour.GREEN,
                Colour.ORANGE, Colour.BLUE, Colour.RED,
                Colour.BLUE, Colour.RED, Colour.ORANGE,
            ],
            [
                Colour.RED, Colour.GREEN, Colour.RED,
                Colour.YELLOW, Colour.YELLOW, Colour.WHITE,
                Colour.RED, Colour.RED, Colour.GREEN
            ]
        ]
        self.assertEqual(self.initial_cube.faces, expected_faces_after_U_prime, "The faces are incorrect for U' move")

if __name__ == '__main__':
    unittest.main()
