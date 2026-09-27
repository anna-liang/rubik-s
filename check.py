from model.cube import Colour

def is_cross_complete():
    """
    Check if the cross is complete.
    Returns True if the cross is complete, False otherwise.
    """
    # Implementation logic here
    pass

def is_f2l_complete():
    """
    Check if the F2L (First Two Layers) is complete.
    Returns True if the F2L is complete, False otherwise.
    """
    # Implementation logic here
    pass

def is_oll_complete():
    """
    Check if the OLL (Orientation of the Last Layer) is complete.
    Returns True if the OLL is complete, False otherwise.
    """
    # Implementation logic here
    pass

# def is_pll_complete():
#     """
#     Check if the PLL (Permutation of the Last Layer) is complete.
#     Returns True if the PLL is complete, False otherwise.
#     """
#     # PLL is completed when cube is solved

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
