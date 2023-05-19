import numpy as np
import math


R_count = 6
c_count = 7
AGENT = 0
COMPUTER = 1
EMPTY = 0
AGENT_PIECE = 1
COMPUTER_PIECE = 2
WINDOW_SIZE = 4

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

def score_arrangement(mainBoard, piece):
    new_score = 0


    center_column = [int(i) for i in list(mainBoard[:, c_count//2])]
    center_count = center_column.count(piece)
    new_score += center_count * 3


    for row in range(R_count):
        row_array = [int(i) for i in list(mainBoard[row,:])]
        for col in range(c_count-3):
            window = row_array[col:col+WINDOW_SIZE]
            new_score += get_window_score(window, piece)


    for col1 in range(c_count):
        column_array = [int(i) for i in list(mainBoard[:,col1])]
        for row1 in range(R_count-3):
            window = column_array[row1:row1+WINDOW_SIZE]
            new_score += get_window_score(window, piece)


    for row2 in range(R_count-3):
        for col2 in range(c_count-3):
            window = [mainBoard[row2+i][col2+i] for i in range(WINDOW_SIZE)]
            new_score += get_window_score(window, piece)

    for row3 in range(R_count-3):
        for col3 in range(c_count-3):
            window = [mainBoard[row3+3-i][col3+i] for i in range(WINDOW_SIZE)]
            new_score += get_window_score(window, piece)

    return new_score

def is_final_state(mainBoard):
    return check_winning_state(mainBoard, AGENT_PIECE) or check_winning_state(mainBoard, COMPUTER_PIECE) or len(find_possible_locations(mainBoard)) == 0

def find_possible_locations(mainBoard):
    valid_locations = []
    for column in range(c_count):
        if check_empty_location(mainBoard, column):
            valid_locations.append(column)
    return valid_locations


def minimax_algorithm(mainBoard, depth, alpha, beta, maximizingAgent):
    possible_locations = find_possible_locations(mainBoard)
    is_final = is_final_state(mainBoard)
    if depth == 0 or is_final:
        if is_final:
            if check_winning_state(mainBoard, AGENT_PIECE):
                return (None, -10000000000000)
            elif check_winning_state(mainBoard, COMPUTER_PIECE):
                return (None, 100000000000000)
            else: 
                return (None, 0)
        else: 
            return (None, score_arrangement(mainBoard, COMPUTER_PIECE))
    if maximizingAgent:
        val = -math.inf
        best_column = 0
        for column in possible_locations:
            row = get_first_empty_row(mainBoard, column)
            board_copy = mainBoard.copy()
            addConnect4Piece(board_copy, row, column, COMPUTER_PIECE)
            new_score = minimax_algorithm(board_copy, depth-1, alpha, beta, False)[1]
            if new_score > val:
                val = new_score
                best_column = column
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return best_column, val

    else:
        val = math.inf
        best_column = 0
        for column in possible_locations:
            row = get_first_empty_row(mainBoard, column)
            board_copy = mainBoard.copy()
            addConnect4Piece(board_copy, row, column, AGENT_PIECE)
            new_score = minimax_algorithm(board_copy, depth-1, alpha, beta, True)[1]
            if new_score < val:
                val = new_score
                best_column = column
            beta = min(beta, val)
            if alpha >= beta:
                break
        return best_column, val