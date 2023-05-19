import numpy as np


R_count = 6

def flip_mainBoard(mainBoard):
    # Initializing a numpy 2D array from the board
    mainBoard_copy = np.array(mainBoard)
    # Fliping the board
    mainBoard_copy = np.flip(mainBoard_copy, 0)
    return mainBoard_copy

def addConnect4Piece(mainBoard, row, column, addedPiece):
    mainBoard[row][column] = addedPiece

def check_empty_location(mainBoard, column):
    return mainBoard[R_count-1][column] == 0

def get_first_empty_row(mainBoard, column):
    for row in range(R_count):
        if mainBoard[row][column] == 0:
            return row