import constants.pll_algorithms as pll_algorithms
from algorithms.algorithms import apply_algorithm

def pll(cube):
    faces = cube.faces
    if (faces[1][2] == faces[3][4] and faces[4][0] == faces[2][4] and 
        faces[2][0] == faces[4][4] and faces[3][2] == faces[1][4]):
        apply_algorithm(cube, pll_algorithms.diagonal_corner_swap)
    elif (faces[1][2] == faces[4][4] and faces[4][0] == faces[3][4] and
          faces[4][2] == faces[1][4] and faces[3][0] == faces[4][4] and
          faces[2][0] == faces[2][4] and faces[2][2] == faces[2][4]):
        apply_algorithm(cube, pll_algorithms.vertical_corner_swap)
    elif faces[1][1] == faces[4][4] and faces[4][1] == faces[2][4] and faces[2][1] == faces[1][4]:
        apply_algorithm(cube, pll_algorithms.triangle_ccw)
    elif faces[1][1] == faces[2][4] and faces[2][1] == faces[4][4] and faces[4][1] == faces[1][4]:
        apply_algorithm(cube, pll_algorithms.triangle_cw)
    elif (faces[1][1] == faces[3][4] and faces[3][1] == faces[1][4] and
          faces[2][1] == faces[4][4] and faces[4][1] == faces[2][4]):
        apply_algorithm(cube, pll_algorithms.cross_swap)
    elif (faces[1][1] == faces[4][4] and faces[4][1] == faces[1][4] and
        faces[2][1] == faces[3][4] and faces[3][1] == faces[2][4]):
        apply_algorithm(cube, pll_algorithms.diagonal_edge_swap)
