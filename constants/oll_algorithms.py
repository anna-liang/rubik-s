from constants.algorithm import Moves

dot = [
    Moves.F, Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME, Moves.F_PRIME
]

l = [
    Moves.F, Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME,
    Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME, Moves.F_PRIME
]

line = [
    Moves.F, Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME, Moves.F_PRIME
]

t = [
    Moves.R, Moves.R, Moves.D, Moves.R_PRIME, Moves.U,
    Moves.U, Moves.R, Moves.D_PRIME, Moves.R_PRIME, Moves.U,
    Moves.U, Moves.R_PRIME
    ]

right_corners = [
    Moves.L_WIDE_PRIME, Moves.U_PRIME, Moves.L, Moves.U,
    Moves.R, Moves.U_PRIME, Moves.R_WIDE_PRIME, Moves.F
]

diagonal_corner = [
    Moves.R_PRIME, Moves.F, Moves.R, Moves.B_PRIME,
    Moves.R_PRIME, Moves.F_PRIME, Moves.R, Moves.B
]

bottom_left_fish = [
    Moves.R, Moves.U, Moves.R_PRIME, Moves.U, 
    Moves.R, Moves.U, Moves.U, Moves.R_PRIME
]

top_right_fish = [
    Moves.R, Moves.U, Moves.U, Moves.R_PRIME,
    Moves.U_PRIME, Moves.R, Moves.U_PRIME, Moves.R_PRIME
]

car = [
    Moves.R, Moves.U, Moves.U, Moves.R, Moves.R,
    Moves.U_PRIME, Moves.R, Moves.R, Moves.U_PRIME,
    Moves.R, Moves.R, Moves.U, Moves.U, Moves.R
]

h = [
    Moves.R, Moves.U, Moves.U, Moves.R_PRIME, Moves.U_PRIME,
    Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME, Moves.R,
    Moves.U_PRIME, Moves.R_PRIME
]
