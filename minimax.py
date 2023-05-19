import numpy as np


R_count = 6
c_count = 7
AGENT = 0
COMPUTER = 1
EMPTY = 0
AGENT_PIECE = 1
COMPUTER_PIECE = 2

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

             
def check_winning_state(mainBoard, checkedPiece):
    for col in range(c_count-3):
        for row in range(R_count):
            if mainBoard[row][col] == checkedPiece\
                    and mainBoard[row][col + 1] == checkedPiece and mainBoard[row][col + 2] == checkedPiece and mainBoard[row][col + 3] == checkedPiece:
                return True

    for col in range(c_count):
        for row in range(R_count-3):
            if mainBoard[row][col] == checkedPiece and mainBoard[row + 1][col] == checkedPiece and mainBoard[row + 2][col] == checkedPiece and mainBoard[row + 3][col] == checkedPiece:
                return True


    for col in range(c_count - 3):
        for row in range(R_count - 3):
            if mainBoard[row][col] == checkedPiece and mainBoard[row + 1][col + 1] == checkedPiece and \
                    mainBoard[row + 2][col + 2] == checkedPiece and mainBoard[row + 3][col + 3] == checkedPiece:
                return True


    for col in range(c_count - 3):
        for row in range(3, R_count):
            if mainBoard[row][col] == checkedPiece and mainBoard[row - 1][col + 1] == checkedPiece and \
                    mainBoard[row - 2][col + 2] == checkedPiece and mainBoard[row - 3][col + 3] == checkedPiece:
                return True

    def get_window_score(window, piece):
        score = 0
        opponent_piece = AGENT_PIECE
        if piece == AGENT_PIECE:
            opponent_piece = COMPUTER_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

