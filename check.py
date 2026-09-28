from model.cube import Colour

def is_cross_complete(cube):
    """
    Check if the cross is complete.
    Returns True if the cross is complete, False otherwise.
    """
    faces = cube.faces
    return (faces[5][4] == faces[5][1] and faces[5][4] == faces[5][3] and
        faces[5][4] == faces[5][7] and faces[5][4] == faces[5][5])

def is_f2l_complete(cube):
    """
    Check if the F2L (First Two Layers) is complete.
    Returns True if the F2L is complete, False otherwise.
    """
    faces = cube.faces
    # check bottom face is completely done
    bottom_face_complete = all(x == faces[5][0] for x in faces[5])
    # check first two rows on all sides are done ([i][3:] where i from 1-4, all same colours for every i)
    for i in range(1, 5):
        if not all(x == faces[i][4] for x in faces[i][3:]):
            return False
    return bottom_face_complete

def is_oll_complete(cube):
    """
    Check if the OLL (Orientation of the Last Layer) is complete.
    Returns True if the OLL is complete, False otherwise.
    """
    faces = cube.faces
    # check top face is completely done
    top_face_complete = all(x == faces[0][0] for x in faces[0])
    return top_face_complete


def is_cube_solved(cube):
    """
    Check if the cube is solved.
    Returns True if the cube is solved, False otherwise.
    """
    # TODO: stricter, but ensure that colour layout makes sense (i.e. yellow can't be next to white)
    colour_set = set(Colour)
    faces_set = set()
    for face in cube.faces:
        if all(colour == face[0] for colour in face):
            faces_set.add(face[0])
        else:
            return False
    return colour_set.issubset(faces_set)
