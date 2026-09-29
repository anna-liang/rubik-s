import constants.oll_algorithms as oll_algorithms
from algorithms.algorithms import apply_algorithm

def oll(cube):
    faces = cube.faces
    face_colour = faces[0][4]
    if (all(x == face_colour for x in (faces[0][0:6] + [faces[0][7]])) and 
          all(x != face_colour for x in ([faces[0][6], faces[0][8]]))):
        apply_algorithm(cube, oll_algorithms.t)
    elif (all(x == face_colour for x in (faces[0][0:2] + faces[0][3:6] + faces[0][6:8] + [faces[1][2], faces[3][0]])) and
          faces[0][2] != face_colour and faces[0][8] != face_colour):
        apply_algorithm(cube, oll_algorithms.right_corners)
    elif (all(x == face_colour for x in (faces[0][0:2] + faces[0][3:6] + faces[0][7:9] + [faces[1][0], faces[4][2]])) and
          faces[0][2] != face_colour and faces[0][6] != face_colour):
        apply_algorithm(cube, oll_algorithms.diagonal_corners)
    elif (all(x == face_colour for x in ([faces[0][1]] + faces[0][3:6] + faces[0][6:8] + [faces[1][2], faces[4][2], faces[3][2]])) and
          faces[0][0] != face_colour and faces[0][2] != face_colour and faces[0][8] != face_colour):
        apply_algorithm(cube, oll_algorithms.bottom_left_fish)
    elif (all(x == face_colour for x in (faces[0][1:3] + faces[0][3:6] + [faces[0][7], faces[2][0], faces[1][0], faces[4][0]])) and
          faces[0][0] != face_colour and faces[0][6] != face_colour and faces[0][8] != face_colour):
        apply_algorithm(cube, oll_algorithms.top_right_fish)
    elif (all(x == face_colour for x in ([faces[0][1]] + faces[0][3:6] + [faces[0][7], faces[2][0], faces[2][2], faces[1][2], faces[3][0]])) and
          faces[0][0] != face_colour and faces[0][2] != face_colour and faces[0][6] != face_colour and faces[0][8] != face_colour):
        apply_algorithm(cube, oll_algorithms.car)
    elif (all(x == face_colour for x in ([faces[0][1]] + faces[0][3:6] + [faces[0][7], faces[1][0], faces[1][2], faces[3][0], faces[3][2]])) and
          faces[0][0] != face_colour and faces[0][2] != face_colour and faces[0][6] != face_colour and faces[0][8] != face_colour):
        apply_algorithm(cube, oll_algorithms.h)
    elif (all(x == face_colour for x in (faces[0][3:6]))):
        apply_algorithm(cube, oll_algorithms.line)
    elif ((faces[0][5] == face_colour and faces[0][7] == face_colour)):
        apply_algorithm(cube, oll_algorithms.l)
    else:
        apply_algorithm(cube, oll_algorithms.dot)
