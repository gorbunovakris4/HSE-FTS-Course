class Minimax:

    def __init__(self, size):
        self.max_depth = Minimax.calc_max_depth(size)
        self.max_score = 10

    @staticmethod
    def calc_max_depth(size):
        if size == 3:
            return 9
        if size == 4:
            return 3
        if size == 5:
            return 3
        return 2

    def __call__(self, board, player=1, depth=0):
        # check max depth
        coordinates = (None, None)
        if depth == self.max_depth:
            winner = board.get_winner()
            if winner == 1:
                return self.max_score - depth, coordinates
            if winner == 0:
                return -self.max_score + depth, coordinates
            if winner == 2:
                return depth, coordinates
            return 0, coordinates

        score = None

        moves = board.empty_cells()

        for (i, j) in moves:

            board.set(i, j, player)

            winner = board.get_winner()
            if winner >= 0:
                board.free(i, j)
                if winner == 1:
                    return self.max_score - depth, (i, j)
                if winner == 0:
                    return -self.max_score + depth, (i, j)
                if winner == 2:
                    return depth, (i, j)

            if board.is_full():
                board.free(i, j)
                return depth, (i, j)

            rec, _ = self.__call__(board, (player + 1) % 2, depth + 1)
            board.free(i, j)

            if player and (score is None or rec > score):
                score = rec
                coordinates = (i, j)

            if not player and (score is None or rec < score):
                score = -rec
                coordinates = (i, j)

        if not score:
            return -1, coordinates

        return score, coordinates
