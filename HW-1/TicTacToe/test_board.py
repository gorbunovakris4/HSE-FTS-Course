from Board import Board

def test_create():
    board = Board(1)
    assert board.size == 1
    assert board.board == [[-1]]
    
def test_set():
    board = Board(2)
    assert board.board[1][1] == -1
    assert board.set(1, 1, 0)
    assert board.board[1][1] == 0

    assert not board.set(1, 1)

    assert not board.set(2, 2)

def test_free():
    board = Board(2)
    board.set(1, 1, 0)
    board.free(1, 1)
    assert board.board[1][1] == -1

def test_is_empty():
    board = Board(2)
    board.set(1, 1, 0)
    assert not board.is_empty(1, 1)
    assert board.is_empty(1, 0)

def test_empty_cells():
    board = Board(2)
    board.set(1, 0, 0)
    board.set(0, 1, 1)
    empty = board.empty_cells()
    assert empty == set([(0, 0), (1, 1)])

def test_need_in_row():
    assert Board(3).need_in_row() == 3
    assert Board(4).need_in_row() == 4
    assert Board(5).need_in_row() == 5
    assert Board(10).need_in_row() == 5

def test_is_valid_coordinates():
    board = Board(2)
    assert board.is_valid_coordinates(0, 0)
    assert board.is_valid_coordinates(1, 1)
    assert not board.is_valid_coordinates(1, 2)
    assert not board.is_valid_coordinates(2, 1)
    assert not board.is_valid_coordinates(-1, 0)
    assert not board.is_valid_coordinates(-1, 2)

def test_get_winner():
    board = Board(3)

    board.set(0, 0, 0)
    board.set(1, 1, 0)
    board.set(2, 2, 0)

    assert board.get_winner() == 0

    board = Board(3)

    board.set(0, 0, 0)
    board.set(0, 1, 0)
    board.set(0, 2, 0)

    assert board.get_winner() == 0

    board = Board(3)

    board.set(0, 0, 1)
    board.set(1, 0, 1)
    board.set(2, 0, 1)

    assert board.get_winner() == 1

    board = Board(3)

    board.set(0, 0, 0)
    board.set(1, 1, 0)
    board.set(2, 2, 1)

    assert board.get_winner() == -1

def test_is_full():
    board = Board(2)

    assert not board.is_full()

    board.set(0, 0, 1)
    board.set(0, 1, 1)
    board.set(1, 0, 0)

    assert not board.is_full()

    board.set(1, 1, 0)

    assert board.is_full()