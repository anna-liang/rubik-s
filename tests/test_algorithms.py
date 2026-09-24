import unittest
import algorithms
from model.cube import Colour
from model.algorithm import Moves

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.initial_cube_faces = [
            [Colour.WHITE] * 9, 
            [Colour.RED] * 9, 
            [Colour.GREEN] * 9, 
            [Colour.ORANGE] * 9, 
            [Colour.BLUE] * 9,
            [Colour.YELLOW] * 9
        ]

    def test_apply_U_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.U)
        expected_faces_after_U = [
            [Colour.WHITE] * 9, 
            [Colour.BLUE] * 3 + [Colour.RED] * 6, 
            [Colour.RED] * 3 + [Colour.GREEN] * 6, 
            [Colour.GREEN] * 3 + [Colour.ORANGE] * 6, 
            [Colour.ORANGE] * 3 + [Colour.BLUE] * 6, 
            [Colour.YELLOW] * 9
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_U, "The faces are incorrect for U move")

    def test_apply_U_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.U_PRIME)
        expected_faces_after_U_prime = [
            [Colour.WHITE] * 9, 
            [Colour.GREEN] * 3 + [Colour.RED] * 6, 
            [Colour.ORANGE] * 3 + [Colour.GREEN] * 6, 
            [Colour.BLUE] * 3 + [Colour.ORANGE] * 6, 
            [Colour.RED] * 3 + [Colour.BLUE] * 6, 
            [Colour.YELLOW] * 9
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_U_prime, "The faces are incorrect for U' move")

    def test_apply_F_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.F)
        expected_faces_after_F = [
            ([Colour.WHITE] * 6 + [Colour.GREEN] * 3),
            [Colour.RED] * 9,
            ([Colour.GREEN] * 2 + [Colour.YELLOW]) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.WHITE] + [Colour.BLUE] * 2) * 3,
            ([Colour.BLUE] * 3 + [Colour.YELLOW] * 6)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_F, "The faces are incorrect for F move")

    def test_apply_F_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.F_PRIME)
        expected_faces_after_F_prime = [
            ([Colour.WHITE] * 6 + [Colour.BLUE] * 3),
            [Colour.RED] * 9,
            ([Colour.GREEN] * 2 + [Colour.WHITE]) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.YELLOW] + [Colour.BLUE] * 2) * 3,
            ([Colour.GREEN] * 3 + [Colour.YELLOW] * 6)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_F_prime, "The faces are incorrect for F' move")
    
    def test_apply_L_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.L)
        expected_faces_after_L = [
            ([Colour.ORANGE] + [Colour.WHITE] * 2) * 3,
            ([Colour.WHITE] + [Colour.RED] * 2) * 3,
            [Colour.GREEN] * 9,
            ([Colour.ORANGE] * 2 + [Colour.YELLOW]) * 3,
            [Colour.BLUE] * 9,
            ([Colour.RED] + [Colour.YELLOW] * 2) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_L, "The faces are incorrect for L move")

    def test_apply_L_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.L_PRIME)
        expected_faces_after_L_prime = [
            ([Colour.RED] + [Colour.WHITE] * 2) * 3,
            ([Colour.YELLOW] + [Colour.RED] * 2) * 3,
            [Colour.GREEN] * 9,
            ([Colour.ORANGE] * 2 + [Colour.WHITE]) * 3,
            [Colour.BLUE] * 9,
            ([Colour.ORANGE] + [Colour.YELLOW] * 2) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_L_prime, "The faces are incorrect for L' move")

    def test_apply_B_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.B)
        expected_faces_after_B = [
            ([Colour.BLUE] * 3 + [Colour.WHITE] * 6),
            [Colour.RED] * 9,
            ([Colour.WHITE] + [Colour.GREEN] * 2) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.BLUE] * 2 + [Colour.YELLOW]) * 3,
            ([Colour.YELLOW] * 6 + [Colour.GREEN] * 3)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_B, "The faces are incorrect for B move")
    
    def test_apply_B_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.B_PRIME)
        expected_faces_after_B_prime = [
            ([Colour.GREEN] * 3 + [Colour.WHITE] * 6),
            [Colour.RED] * 9,
            ([Colour.YELLOW] + [Colour.GREEN] * 2) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.BLUE] * 2 + [Colour.WHITE]) * 3,
            ([Colour.YELLOW] * 6 + [Colour.BLUE] * 3),
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_B_prime, "The faces are incorrect for B' move")

    def test_apply_R_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.R)
        expected_faces_after_R = [
            ([Colour.WHITE] * 2 + [Colour.RED]) * 3,
            ([Colour.RED] * 2 + [Colour.YELLOW]) * 3,
            [Colour.GREEN] * 9,
            ([Colour.WHITE] + [Colour.ORANGE] * 2) * 3,
            [Colour.BLUE] * 9,
            ([Colour.YELLOW] * 2 + [Colour.ORANGE]) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_R, "The faces are incorrect for R move")
    
    def test_apply_R_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.R_PRIME)
        expected_faces_after_R_prime = [
            ([Colour.WHITE] * 2 + [Colour.ORANGE]) * 3,
            ([Colour.RED] * 2 + [Colour.WHITE]) * 3,
            [Colour.GREEN] * 9,
            ([Colour.YELLOW] + [Colour.ORANGE] * 2) * 3,
            [Colour.BLUE] * 9,
            ([Colour.YELLOW] * 2 + [Colour.RED]) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_R_prime, "The faces are incorrect for R' move")

    def test_apply_D_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.D)
        expected_faces_after_D = [
            [Colour.WHITE] * 9, 
            [Colour.RED] * 6 + [Colour.GREEN] * 3, 
            [Colour.GREEN] * 6 + [Colour.ORANGE] * 3,
            [Colour.ORANGE] * 6 + [Colour.BLUE] * 3,
            [Colour.BLUE] * 6 + [Colour.RED] * 3,
            [Colour.YELLOW] * 9
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_D, "The faces are incorrect for D move")

    def test_apply_D_prime_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.D_PRIME)
        expected_faces_after_D_prime = [
            [Colour.WHITE] * 9, 
            [Colour.RED] * 6 + [Colour.BLUE] * 3, 
            [Colour.GREEN] * 6 + [Colour.RED] * 3,
            [Colour.ORANGE] * 6 + [Colour.GREEN] * 3,
            [Colour.BLUE] * 6 + [Colour.ORANGE] * 3,
            [Colour.YELLOW] * 9
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_D_prime, "The faces are incorrect for D' move")

    def test_apply_M_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.M)
        expected_faces_after_M = [
            ([Colour.WHITE, Colour.RED, Colour.WHITE] * 3),
            ([Colour.RED, Colour.YELLOW, Colour.RED] * 3),
            [Colour.GREEN] * 9,
            ([Colour.ORANGE, Colour.WHITE, Colour.ORANGE] * 3),
            [Colour.BLUE] * 9,
            ([Colour.YELLOW, Colour.ORANGE, Colour.YELLOW] * 3)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_M, "The faces are incorrect for M move")

    def test_apply_M_move(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.M_PRIME)
        expected_faces_after_M_prime = [
            ([Colour.WHITE, Colour.ORANGE, Colour.WHITE] * 3),
            ([Colour.RED, Colour.WHITE, Colour.RED] * 3),
            [Colour.GREEN] * 9,
            ([Colour.ORANGE, Colour.YELLOW, Colour.ORANGE] * 3),
            [Colour.BLUE] * 9,
            ([Colour.YELLOW, Colour.RED, Colour.YELLOW] * 3)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_M_prime, "The faces are incorrect for M' move")

    def test_apply_U_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.U_WIDE)
        expected_faces_after_U_wide = [
            [Colour.WHITE] * 9,
            [Colour.BLUE] * 6 + [Colour.RED] * 3, 
            [Colour.RED] * 6 + [Colour.GREEN] * 3,
            [Colour.GREEN] * 6 + [Colour.ORANGE] * 3,
            [Colour.ORANGE] * 6 + [Colour.BLUE] * 3,
            [Colour.YELLOW] * 9,
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_U_wide, "The faces are incorrect for Uw move")

    def test_apply_D_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.D_WIDE)
        expected_faces_after_D_wide = [
            [Colour.WHITE] * 9,
            [Colour.RED] * 3 + [Colour.GREEN] * 6, 
            [Colour.GREEN] * 3 + [Colour.ORANGE] * 6, 
            [Colour.ORANGE] * 3 + [Colour.BLUE] * 6, 
            [Colour.BLUE] * 3 + [Colour.RED] * 6, 
            [Colour.YELLOW] * 9,
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_D_wide, "The faces are incorrect for Dw move")

    def test_apply_L_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.L_WIDE)
        expected_faces_after_L_wide = [
            ([Colour.ORANGE] * 2 + [Colour.WHITE]) * 3,
            ([Colour.WHITE] * 2 + [Colour.RED]) * 3,
            [Colour.GREEN] * 9,
            ([Colour.ORANGE] + [Colour.YELLOW] * 2) * 3,
            [Colour.BLUE] * 9,
            ([Colour.RED] * 2 + [Colour.YELLOW]) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_L_wide, "The faces are incorrect for Lw move")

    def test_apply_R_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.R_WIDE)
        expected_faces_after_R_wide = [
            ([Colour.WHITE] + [Colour.RED] * 2) * 3,
            ([Colour.RED] + [Colour.YELLOW] * 2) * 3,
            [Colour.GREEN] * 9,
            ([Colour.WHITE] * 2 + [Colour.ORANGE]) * 3,
            [Colour.BLUE] * 9,
            ([Colour.YELLOW] + [Colour.ORANGE] * 2) * 3
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_R_wide, "The faces are incorrect for Rw move")

    def test_apply_F_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.F_WIDE)
        expected_faces_after_F_wide = [
            ([Colour.WHITE] * 3 + [Colour.GREEN] * 6),
            [Colour.RED] * 9,
            ([Colour.GREEN] + [Colour.YELLOW] * 2) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.WHITE] * 2 + [Colour.BLUE]) * 3,
            ([Colour.BLUE] * 6 + [Colour.YELLOW] * 3)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_F_wide, "The faces are incorrect for Fw move")

    def test_apply_B_wide(self):
        algorithms.apply_move(self.initial_cube_faces, Moves.B_WIDE)
        expected_faces_after_B_wide = [
            ([Colour.BLUE] * 6 + [Colour.WHITE] * 3),
            [Colour.RED] * 9,
            ([Colour.WHITE] * 2 + [Colour.GREEN]) * 3,
            [Colour.ORANGE] * 9,
            ([Colour.BLUE] + [Colour.YELLOW] * 2) * 3,
            ([Colour.YELLOW] * 3 + [Colour.GREEN] * 6)
        ]
        self.assertEqual(self.initial_cube_faces, expected_faces_after_B_wide, "The faces are incorrect for Bw move")

if __name__ == '__main__':
    unittest.main()
