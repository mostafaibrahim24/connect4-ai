import numpy as np

def flip_mainBoard(mainBoard):
    # Initializing a numpy 2D array from the board
    mainBoard_copy = np.array(mainBoard)
    # Fliping the board
    mainBoard_copy = np.flip(mainBoard_copy, 0)
    return mainBoard_copy