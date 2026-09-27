from constants.algorithm import Moves

diagonal_corner_swap = [
    Moves.F, Moves.R, Moves.U_PRIME, Moves.R_PRIME, 
    Moves.U_PRIME, Moves.R, Moves.U, Moves.R_PRIME, 
    Moves.F_PRIME, Moves.R, Moves.U, Moves.R_PRIME, 
    Moves.U_PRIME, Moves.R_PRIME, Moves.F, Moves.R, 
    Moves.F_PRIME
   ]

vertical_corner_swap = [
    Moves.R, Moves.U, Moves.R_PRIME, Moves.U_PRIME,
    Moves.R_PRIME, Moves.F, Moves.R, Moves.R, Moves.U_PRIME,
    Moves.R_PRIME, Moves.U_PRIME, Moves.R, Moves.U,
    Moves.R_PRIME, Moves.F_PRIME
]

triangle_ccw = [
    Moves.R, Moves.U_PRIME, Moves.R, Moves.U, Moves.R,
    Moves.U, Moves.R, Moves.U_PRIME, Moves.R_PRIME,
    Moves.U_PRIME, Moves.R, Moves.R
]

triangle_cw = [
    Moves.R, Moves.R, Moves.U, Moves.R, Moves.U,
    Moves.R_PRIME, Moves.U_PRIME, Moves.R_PRIME,
    Moves.U_PRIME, Moves.R_PRIME, Moves.U, Moves.R_PRIME
]

cross_swap = [
    Moves.M, Moves.M, Moves.U, Moves.M, Moves.M, Moves.U,
    Moves.U, Moves.M, Moves.M, Moves.U, Moves.M, Moves.M
]

diagonal_edge_swap = [
    Moves.M, Moves.M, Moves. U, Moves.M, Moves.M, Moves.U,
    Moves.M_PRIME, Moves.U, Moves.U, Moves.M, Moves.M,
    Moves.U, Moves.U, Moves.M_PRIME, Moves.U, Moves.U
]
