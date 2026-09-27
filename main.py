import check, algorithms.algorithms as algorithms, random
from model.cube import Cube, Colour
from constants.algorithm import Moves

def build_cube():
    """
    Build the cube representation.
    This function initializes the cube to its solved state.
    """
    top = [Colour.WHITE] * 9
    front = [Colour.RED] * 9
    left = [Colour.GREEN] * 9
    back = [Colour.ORANGE] * 9
    right = [Colour.BLUE] * 9
    bottom = [Colour.YELLOW] * 9
    cube = Cube([top, front, left, back, right, bottom])
    return cube

def solve():
    if not check.is_cross_complete():
        algorithms.cross()
    if not check.is_f2l_complete():
        algorithms.f2l()
    if not check.is_oll_complete():
        algorithms.oll()
    if not check.is_pll_complete():
        algorithms.pll()
    if not check.is_cube_solved():
        raise Exception("Cube is not solved after applying all algorithms.")


if __name__ == "__main__":
    # scramble.scramble(random.randint(10, 30))  # Scramble the cube with a random number of moves between 10 and 30
    cube = build_cube()
    # print(cube)
    check.is_cube_solved(cube)
    # algorithms.apply_move(cube.faces, Moves.U_PRIME)
    print(cube)
    # solve()