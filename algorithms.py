from model.algorithm import Moves

def apply_move(faces, move):
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
        case Moves.U_PRIME:
            # Rotate the top layer counter-clockwise
            temp = faces[1][0:3]
            faces[1][0:3] = faces[2][0:3]
            faces[2][0:3] = faces[3][0:3]
            faces[3][0:3] = faces[4][0:3]
            faces[4][0:3] = temp
        case Moves.D:
            temp = faces[1][6:9]
            faces[1][6:9] = faces[2][6:9]
            faces[2][6:9] = faces[3][6:9]
            faces[3][6:9] = faces[4][6:9]
            faces[4][6:9] = temp
        case Moves.D_PRIME:
            temp = faces[1][6:9]
            faces[1][6:9] = faces[4][6:9]
            faces[4][6:9] = faces[3][6:9]
            faces[3][6:9] = faces[2][6:9]
            faces[2][6:9] = temp
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
            faces[3][6] = temp[2]
            faces[3][3] = temp[1]
            faces[3][0] = temp[0]
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
        case Moves.F:
            temp = [faces[0][6], faces[0][7], faces[0][8]]
            faces[0][6] = faces[2][2]
            faces[0][7] = faces[2][5]
            faces[0][8] = faces[2][8]
            faces[2][2] = faces[5][0]
            faces[2][5] = faces[5][1]
            faces[2][8] = faces[5][2]
            faces[5][1] = faces[4][6]
            faces[5][2] = faces[4][3]
            faces[5][3] = faces[4][0]
            faces[4][0] = temp[0]
            faces[4][3] = temp[1]
            faces[4][6] = temp[2]
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
            faces[2][0] = temp[2]
            faces[2][3] = temp[1]
            faces[2][6] = temp[0]
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
        case _:
            raise ValueError(f"Move {move} not implemented yet.")

def cross():
    """
    Perform the cross algorithm on the cube.
    This function will manipulate the cube to solve the cross.
    """
    # Implementation logic here
    pass

def f2l():
    """
    Perform the F2L (First Two Layers) algorithm on the cube.
    This function will manipulate the cube to solve the first two layers.
    """
    # Implementation logic here
    pass

def oll():
    """
    Perform the OLL (Orientation of the Last Layer) algorithm on the cube.
    This function will manipulate the cube to orient the last layer correctly.
    """
    # Implementation logic here
    pass

def pll():
    """
    Perform the PLL (Permutation of the Last Layer) algorithm on the cube.
    This function will manipulate the cube to permute the last layer correctly.
    """
    # Implementation logic here
    pass
