from Board import Board

from copy import deepcopy

def max_depth(size):
    if size == 3:
        return 9
    if size == 4:
        return 3
    if size == 5:
        return 3
    return 2

MAX_DEPTH = -1

def minimax(board, player=1, depth=0):

    # check max depth
    if depth == MAX_DEPTH:
        winner = board.get_winner()
        if winner == 1:
            return 10 - depth, (None, None)
        if winner == 0:
            return -10 + depth, (None, None)
        if winner == 2:
            return depth, (None, None)
        return 0, (None, None)

    score = None
    coordinates = (None, None)

    moves = board.empty_cells()

    for (i, j) in moves:

        board.set(i, j, player)

        winner = board.get_winner()
        if winner >= 0:
            board.free(i, j)
            if winner == 1:
                return 10 - depth, (i, j)
            if winner == 0:
                return + -10 + depth, (i, j)
            if winner == 2:
                return depth, (i, j)

        if board.is_full():
            board.free(i, j)
            return depth, (i, j)

        rec, _ = minimax(board, (player + 1) % 2, depth + 1)
        board.free(i, j)

        if player and (score == None or rec > score):
            score = rec
            coordinates = (i, j)

        if not player and (score == None or rec < score):
            score = -rec
            coordinates = (i, j)

    if not score:
        return -1, coordinates

    return score, coordinates