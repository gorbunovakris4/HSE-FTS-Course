class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[-1] * size for _ in range(size)]

    def set(self, i, j, player=0):

        if not self.is_valid_coordinates(i, j):
            print("This is not a valid coordinates!")
            return 0

        if not self.is_empty(i, j):
            print("This field is not empty!")
            return 0

        self.board[i][j] = player
        return 1

    def free(self, i, j):
        self.board[i][j] = -1

    def is_empty(self, i, j):
        return self.board[i][j] < 0

    def empty_cells(self):
        moves = set()

        for i in range(self.size):
            for j in range(self.size):
                if self.is_empty(i, j):
                    moves.add((i, j))

        return moves

    def need_in_row(self):
        return min(5, self.size)

    def is_valid_coordinates(self, i, j):
        return min(i, j) >= 0 and max(i, j) < self.size

    # -
    def win_horizontal(self, i, j, need, player):
        if not self.is_valid_coordinates(i, j):
            return False
        if self.board[i][j] != player:
            return False
        if need == 1:
            return True
        return self.win_horizontal(i, j + 1, need - 1, player)

    # |
    def win_vertical(self, i, j, need, player):

        if not self.is_valid_coordinates(i, j):
            return False
        if self.board[i][j] != player:
            return False
        if need == 1:
            return True
        return self.win_vertical(i + 1, j, need - 1, player)

    # \
    def win_diagonal(self, i, j, need, player):
        if not self.is_valid_coordinates(i, j):
            return False
        if self.board[i][j] != player:
            return False
        if need == 1:
            return True
        return self.win_diagonal(i + 1, j + 1, need - 1, player)

    # /
    def win_diagonal_reverse(self, i, j, need, player):
        if not self.is_valid_coordinates(i, j):
            return False
        if self.board[i][j] != player:
            return False
        if need == 1:
            return True
        return self.win_diagonal_reverse(i - 1, j + 1, need - 1, player)

    def get_winner(self):
        need = self.need_in_row()

        for i in range(self.size):
            for j in range(self.size):
                for player in [0, 1]:
                    if self.win_horizontal(i, j, need, player) \
                            or self.win_vertical(i, j, need, player) \
                            or self.win_diagonal(i, j, need, player) \
                            or self.win_diagonal_reverse(i, j, need, player):
                        return player

        return -1

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.is_empty(i, j):
                    return False
        return True

    def board_symbol(self, i, j):
        value = self.board[i][j]
        if value == 0:
            return 'x'
        elif value == 1:
            return 'o'
        else:
            return ' '

    def print(self):

        # top boarder
        print('   ', end='')
        for i in range(self.size):
            print(f'---', end='')
        print('+')

        print('   |', end='')
        for i in range(self.size):
            print(f' {i + 1}|', end='')
        print()

        # content
        for i in range(self.size):
            print('|--', end='')
            for k in range(self.size):
                print(f'+--', end='')
            print('|')

            print(f'| {i + 1}|', end='')
            for j in range(self.size):
                print(f' {self.board_symbol(i, j)}|', end='')

            print()

        # bottom boarder
        print('+--', end='')
        for i in range(self.size):
            print('---', end='')
        print('+')
