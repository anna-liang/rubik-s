from constants.algorithm import Moves

def cw(faces):
    temp = faces[0]
    faces[0] = faces[6]
    faces[6] = faces[8]
    faces[8] = faces[2]
    faces[2] = temp
    temp2 = faces[1]
    faces[1] = faces[3]
    faces[3] = faces[7]
    faces[7] = faces[5]
    faces[5] = temp2

def ccw(faces):
    temp = faces[0]
    faces[0] = faces[2]
    faces[2] = faces[8]
    faces[8] = faces[6]
    faces[6] = temp
    temp2 = faces[1]
    faces[1] = faces[5]
    faces[5] = faces[7]
    faces[7] = faces[3]
    faces[3] = temp2

def apply_move(cube, move):
    faces = cube.faces
    """
    Apply a move to the cube.

    Args:
        faces (list): The faces of the cube.
        move (Moves): The move to apply.

    Returns:
        None
    """
    match move:
        case Moves.U:
            # Rotate the top layer clockwise
            temp = faces[1][0:3]
            faces[1][0:3] = faces[4][0:3]
            faces[4][0:3] = faces[3][0:3]
            faces[3][0:3] = faces[2][0:3]
            faces[2][0:3] = temp
            cw(faces[0])
        case Moves.U_PRIME:
            # Rotate the top layer counter-clockwise
            temp = faces[1][0:3]
            faces[1][0:3] = faces[2][0:3]
            faces[2][0:3] = faces[3][0:3]
            faces[3][0:3] = faces[4][0:3]
            faces[4][0:3] = temp
            ccw(faces[0])
        case Moves.D:
            temp = faces[1][6:9]
            faces[1][6:9] = faces[2][6:9]
            faces[2][6:9] = faces[3][6:9]
            faces[3][6:9] = faces[4][6:9]
            faces[4][6:9] = temp
            cw(faces[5])
        case Moves.D_PRIME:
            temp = faces[1][6:9]
            faces[1][6:9] = faces[4][6:9]
            faces[4][6:9] = faces[3][6:9]
            faces[3][6:9] = faces[2][6:9]
            faces[2][6:9] = temp
            ccw(faces[5])
        case Moves.L:
            temp = [faces[0][0], faces[0][3], faces[0][6]]
            faces[0][0] = faces[3][8]
            faces[0][3] = faces[3][5]
            faces[0][6] = faces[3][2]
            faces[3][2] = faces[5][6]
            faces[3][5] = faces[5][3]
            faces[3][8] = faces[5][0]
            faces[5][0] = faces[1][0]
            faces[5][3] = faces[1][3]
            faces[5][6] = faces[1][6]
            faces[1][0] = temp[0]
            faces[1][3] = temp[1]
            faces[1][6] = temp[2]
            cw(faces[2])
        case Moves.L_PRIME:
            temp = [faces[0][0], faces[0][3], faces[0][6]]
            faces[0][0] = faces[1][0]
            faces[0][3] = faces[1][3]
            faces[0][6] = faces[1][6]
            faces[1][0] = faces[5][0]
            faces[1][3] = faces[5][3]
            faces[1][6] = faces[5][6]
            faces[5][0] = faces[3][8]
            faces[5][3] = faces[3][5]
            faces[5][6] = faces[3][2]
            faces[3][2] = temp[2]
            faces[3][5] = temp[1]
            faces[3][8] = temp[0]
            ccw(faces[2])
        case Moves.R:
            temp = [faces[0][2], faces[0][5], faces[0][8]]
            faces[0][2] = faces[1][2]
            faces[0][5] = faces[1][5]
            faces[0][8] = faces[1][8]
            faces[1][2] = faces[5][2]
            faces[1][5] = faces[5][5]
            faces[1][8] = faces[5][8]
            faces[5][2] = faces[3][6]
            faces[5][5] = faces[3][3]
            faces[5][8] = faces[3][0]
            faces[3][0] = temp[2]
            faces[3][3] = temp[1]
            faces[3][6] = temp[0]
            cw(faces[4])
        case Moves.R_PRIME:
            temp = [faces[0][2], faces[0][5], faces[0][8]]
            faces[0][2] = faces[3][6]
            faces[0][5] = faces[3][3]
            faces[0][8] = faces[3][0]
            faces[3][0] = faces[5][8]
            faces[3][3] = faces[5][5]
            faces[3][6] = faces[5][2]
            faces[5][2] = faces[1][2]
            faces[5][5] = faces[1][5]
            faces[5][8] = faces[1][8]
            faces[1][2] = temp[0]
            faces[1][5] = temp[1]
            faces[1][8] = temp[2]
            ccw(faces[4])
        case Moves.F:
            temp = [faces[0][6], faces[0][7], faces[0][8]]
            faces[0][6] = faces[2][8]
            faces[0][7] = faces[2][5]
            faces[0][8] = faces[2][2]
            faces[2][2] = faces[5][0]
            faces[2][5] = faces[5][1]
            faces[2][8] = faces[5][2]
            faces[5][0] = faces[4][6]
            faces[5][1] = faces[4][3]
            faces[5][2] = faces[4][0]
            faces[4][0] = temp[0]
            faces[4][3] = temp[1]
            faces[4][6] = temp[2]
            cw(faces[1])
        case Moves.F_PRIME:
            temp = [faces[0][6], faces[0][7], faces[0][8]]
            faces[0][6] = faces[4][0]
            faces[0][7] = faces[4][3]
            faces[0][8] = faces[4][6]
            faces[4][0] = faces[5][2]
            faces[4][3] = faces[5][1]
            faces[4][6] = faces[5][0]
            faces[5][0] = faces[2][2]
            faces[5][1] = faces[2][5]
            faces[5][2] = faces[2][8]
            faces[2][2] = temp[2]
            faces[2][5] = temp[1]
            faces[2][8] = temp[0]
            ccw(faces[1])
        case Moves.B:
            temp = [faces[0][0], faces[0][1], faces[0][2]]
            faces[0][0] = faces[4][2]
            faces[0][1] = faces[4][5]
            faces[0][2] = faces[4][8]
            faces[4][2] = faces[5][8]
            faces[4][5] = faces[5][7]
            faces[4][8] = faces[5][6]
            faces[5][6] = faces[2][0]
            faces[5][7] = faces[2][3]
            faces[5][8] = faces[2][6]
            faces[2][0] = temp[2]
            faces[2][3] = temp[1]
            faces[2][6] = temp[0]
            cw(faces[3])
        case Moves.B_PRIME:
            temp = [faces[0][0], faces[0][1], faces[0][2]]
            faces[0][0] = faces[2][6]
            faces[0][1] = faces[2][3]
            faces[0][2] = faces[2][0]
            faces[2][0] = faces[5][6]
            faces[2][3] = faces[5][7]
            faces[2][6] = faces[5][8]
            faces[5][6] = faces[4][8]
            faces[5][7] = faces[4][5]
            faces[5][8] = faces[4][2]
            faces[4][2] = temp[0]
            faces[4][5] = temp[1]
            faces[4][8] = temp[2]
            ccw(faces[3])
        case Moves.M:
            temp = [faces[0][1], faces[0][4], faces[0][7]]
            faces[0][1] = faces[1][1]
            faces[0][4] = faces[1][4]
            faces[0][7] = faces[1][7]
            faces[1][1] = faces[5][1]
            faces[1][4] = faces[5][4]
            faces[1][7] = faces[5][7]
            faces[5][1] = faces[3][7]
            faces[5][4] = faces[3][4]
            faces[5][7] = faces[3][1]
            faces[3][1] = temp[2]
            faces[3][4] = temp[1]
            faces[3][7] = temp[0]
        case Moves.M_PRIME:
            temp = [faces[0][1], faces[0][4], faces[0][7]]
            faces[0][1] = faces[3][7]
            faces[0][4] = faces[3][4]
            faces[0][7] = faces[3][1]
            faces[3][1] = faces[5][7]
            faces[3][4] = faces[5][4]
            faces[3][7] = faces[5][1]
            faces[5][1] = faces[1][1]
            faces[5][4] = faces[1][4]
            faces[5][7] = faces[1][7]
            faces[1][1] = temp[0]
            faces[1][4] = temp[1]
            faces[1][7] = temp[2]
        case Moves.L_WIDE_PRIME:
            temp = [[faces[0][0], faces[0][1]], [faces[0][3], faces[0][4]], [faces[0][6], faces[0][7]]]
            faces[0][0], faces[0][1] = faces[1][0], faces[1][1]
            faces[0][3], faces[0][4] = faces[1][3], faces[1][4]
            faces[0][6], faces[0][7] = faces[1][6], faces[1][7]
            faces[1][0], faces[1][1] = faces[5][0], faces[5][1]
            faces[1][3], faces[1][4] = faces[5][3], faces[5][4]
            faces[1][6], faces[1][7] = faces[5][6], faces[5][7]
            faces[5][0], faces[5][1] = faces[3][8], faces[3][7]
            faces[5][3], faces[5][4] = faces[3][5], faces[3][4]
            faces[5][6], faces[5][7] = faces[3][2], faces[3][1]
            faces[3][2], faces[3][1] = temp[2]
            faces[3][5], faces[3][4] = temp[1]
            faces[3][8], faces[3][7] = temp[0]
            ccw(faces[2])
        case Moves.R_WIDE_PRIME:
            temp = [[faces[0][1], faces[0][2]], [faces[0][4], faces[0][5]], [faces[0][7], faces[0][8]]]
            faces[0][1], faces[0][2] = faces[1][1], faces[1][2]
            faces[0][4], faces[0][5] = faces[1][4], faces[1][5]
            faces[0][7], faces[0][8] = faces[1][7], faces[1][8]
            faces[1][1], faces[1][2] = faces[5][1], faces[5][2]
            faces[1][4], faces[1][5] = faces[5][4], faces[5][5]
            faces[1][7], faces[1][8] = faces[5][7], faces[5][8]
            faces[5][1], faces[5][2] = faces[3][7], faces[3][6]
            faces[5][4], faces[5][5] = faces[3][4], faces[3][3]
            faces[5][7], faces[5][8] = faces[3][1], faces[3][0]
            faces[3][1], faces[3][0] = temp[2]
            faces[3][4], faces[3][3] = temp[1]
            faces[3][7], faces[3][6] = temp[0]
            ccw(faces[4])
        case Moves.F_WIDE:
            temp = [[faces[0][6], faces[0][3]], [faces[0][7], faces[0][4]], [faces[0][8], faces[0][5]]]
            faces[0][6], faces[0][3] = faces[2][8], faces[2][7]
            faces[0][7], faces[0][4] = faces[2][5], faces[2][4]
            faces[0][8], faces[0][5] = faces[2][2], faces[2][1]
            faces[2][1], faces[2][2] = faces[5][3], faces[5][0]
            faces[2][4], faces[2][5] = faces[5][4], faces[5][1]
            faces[2][7], faces[2][8] = faces[5][5], faces[5][2]
            faces[5][0], faces[5][3] = faces[4][6], faces[4][7]
            faces[5][1], faces[5][4] = faces[4][3], faces[4][4]
            faces[5][2], faces[5][5] = faces[4][0], faces[4][1]
            faces[4][0], faces[4][1] = temp[0]
            faces[4][3], faces[4][4] = temp[1]
            faces[4][6], faces[4][7] = temp[2]
            cw(faces[1])
        case Moves.F_WIDE_PRIME:
            temp = [[faces[0][6], faces[0][3]], [faces[0][7], faces[0][4]], [faces[0][8], faces[0][5]]]
            faces[0][3], faces[0][6] = faces[4][0], faces[4][1]
            faces[0][4], faces[0][7] = faces[4][3], faces[4][4]
            faces[0][5], faces[0][8] = faces[4][6], faces[4][7]
            faces[4][0], faces[4][1] = faces[5][2], faces[5][5]
            faces[4][3], faces[4][4] = faces[5][1], faces[5][4]
            faces[4][6], faces[4][7] = faces[5][0], faces[5][3]
            faces[5][0], faces[5][3] = faces[2][1], faces[2][2]
            faces[5][1], faces[5][4] = faces[2][4], faces[2][5]
            faces[5][2], faces[5][5] = faces[2][7], faces[2][8]
            faces[2][1], faces[2][2] = temp[2]
            faces[2][4], faces[2][5] = temp[1]
            faces[2][7], faces[2][8] = temp[0]
            ccw(faces[1])
        case Moves.X:
            # clockwise along R
            temp = faces[0]
            faces[0] = faces[1]
            faces[1] = faces[5]
            faces[5] = faces[3]
            faces[3] = temp
        case Moves.Y:
            # clockwise along U
            temp = faces[1]
            faces[1] = faces[4]
            faces[4] = faces[3]
            faces[3] = faces[2]
            faces[2] = temp
        case Moves.Z:
            # clockwise along F
            temp = faces[0]
            faces[0] = faces[2]
            faces[2] = faces[5]
            faces[5] = faces[4]
            faces[4] = temp
        case _:
            raise ValueError(f"Move {move} not implemented yet.")

def apply_algorithm(cube, algorithm):
    for move in algorithm:
        apply_move(cube, move)