import numpy as np

def flip_board(board):
    # Initializing a numpy 2D array from the board
    board_copy = np.array(board)
    # Fliping the board
    board_copy = np.flip(board_copy, 0)
    return board_copy