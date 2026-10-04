from algorithms.algorithms import apply_algorithm, apply_move
from constants.algorithm import Moves


def orient_and_fill_cross(cube, starting_side):
    """
    Apply a U move until the cross piece on the top face against
    `starting_side` is above where it goes in the cross. Then rotate
    so it fits in the cross.
    """
    face_order = [3, 4, 1, 2]
    faces = cube.faces
    current_index = face_order.index(starting_side)
    while faces[face_order[current_index]][1] != faces[face_order[current_index]][4]:
        apply_move(Moves.U)
        if current_index == len(face_order) - 1:
            current_index = 0
        else:
            current_index += 1
    if current_index == 3:
        apply_move(Moves.B)
        apply_move(Moves.B)
    elif current_index == 4:
        apply_move(Moves.R)
        apply_move(Moves.R)
    elif current_index == 1:
        apply_move(Moves.F)
        apply_move(Moves.F)
    elif current_index == 2:
        apply_move(Moves.L)
        apply_move(Moves.L)

def cross(cube):
    faces = cube.faces
    face_colour = faces[5][4]
    front_top_algo = [Moves.F, Moves.R, Moves.U_PRIME, Moves.R_PRIME, Moves.F_PRIME]
    front_right_algo = [Moves.R, Moves.U, Moves.R_PRIME]
    front_left_algo = [Moves.L_PRIME, Moves.U_PRIME, Moves.L]

    match face_colour:
        case x if x == faces[0][1]:
            orient_and_fill_cross(cube, 3)
        case x if x == faces[0][3]:
            orient_and_fill_cross(cube, 2)
        case x if x == faces[0][5]:
            orient_and_fill_cross(cube, 4)
        case x if x == faces[0][7]:
            orient_and_fill_cross(cube, 1)
        case x if x == faces[1][1]:
            apply_algorithm(front_top_algo)
            orient_and_fill_cross(cube, 3)
        case x if x == faces[1][5]:
            apply_algorithm(front_right_algo)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[1][3]:
            apply_algorithm(front_left_algo)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[2][1]:
            apply_move(Moves.Y_PRIME)
            apply_algorithm(front_top_algo)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 4)
        case x if x == faces[2][5]:
            apply_move(Moves.Y_PRIME)
            apply_algorithm(front_right_algo)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 4)
        case x if x == faces[2][3]:
            apply_move(Moves.Y_PRIME)
            apply_algorithm(front_left_algo)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 4)
        case x if x == faces[3][1]:
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            apply_algorithm(front_top_algo)
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[3][5]:
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            apply_algorithm(front_right_algo)
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[3][3]:
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            apply_algorithm(front_left_algo)
            apply_move(Moves.Y)
            apply_move(Moves.Y)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[4][1]:
            apply_move(Moves.Y)
            apply_algorithm(front_top_algo)
            apply_move(Moves.Y_PRIME)
            orient_and_fill_cross(cube, 2)
        case x if x == faces[4][5]:
            apply_move(Moves.Y)
            apply_algorithm(front_right_algo)
            apply_move(Moves.Y_PRIME)
            orient_and_fill_cross(cube, 2)
        case x if x == faces[4][3]:
            apply_move(Moves.Y)
            apply_algorithm(front_left_algo)
            apply_move(Moves.Y_PRIME)
            orient_and_fill_cross(cube, 2)
        case x if x == faces[5][1]:
            apply_move(Moves.F)
            apply_move(Moves.F)
            orient_and_fill_cross(cube, 1)
        case x if x == faces[5][5]:
            apply_move(Moves.R)
            apply_move(Moves.R)
            orient_and_fill_cross(cube, 4)
        case x if x == faces[5][3]:
            apply_move(Moves.L)
            apply_move(Moves.L)
            orient_and_fill_cross(cube, 2)
        case x if x == faces[5][7]:
            apply_move(Moves.B)
            apply_move(Moves.B)
            orient_and_fill_cross(cube, 3)
        case _:
            raise ValueError(f"Cannot match case for cross edge piece.")

