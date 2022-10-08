from Board import Board
from Minimax import Minimax


class TicTacToe:
    def __init__(self, size):
        self.board = Board(size)
        self.minimax = Minimax(size)

    def make_player_move(self, i, j):
        return self.board.set(i, j, 0)

    def make_move(self):
        _, (i, j) = self.minimax(self.board, 1)
        self.board.set(i, j, 1)

    # 0 - player 0 win
    # 1 - player 1 win
    # 2 - draw
    # -1 - not over
    def is_over(self):
        winner = self.board.get_winner()

        if winner >= 0:
            return winner

        if self.board.is_full():
            return 2

        return -1
