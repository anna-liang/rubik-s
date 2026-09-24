def scramble(num_of_moves):
    """
    Scrambles the cube by performing a series of random moves.

    Args:
        num_of_moves (int): The number of random moves to perform.

    Returns:
        None
    """
    import random

    # Define possible moves
    moves = ['U', 'D', 'L', 'R', 'F', 'B']

    for _ in range(num_of_moves):
        move = random.choice(moves)
        # Perform the move on the cube (this is a placeholder for actual cube manipulation logic)
        print(f"Performing move: {move}")