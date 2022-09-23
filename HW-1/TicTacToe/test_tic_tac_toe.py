from TicTacToe import TicTacToe
from Board import Board

def board_eq(board1, board2):
    return board1.board == board2.board

def test_create():
    game = TicTacToe(3)
    
    assert board_eq(game.board, Board(3))

def test_make_player_move():
    game = TicTacToe(3)

    game.make_player_move(1, 1)
    board = Board(3)
    board.set(1, 1, 0)
    assert board_eq(game.board, board)

def test_make_move():
    game = TicTacToe(3)

    game.make_player_move(0, 0)
    game.make_player_move(1, 1)
    game.make_move()

    board = Board(3)

    board.set(0, 0, 0)
    board.set(1, 1, 0)
    board.set(2, 2, 1)

    assert board_eq(game.board, board)

def test_is_over():
    game = TicTacToe(3)

    game.make_player_move(0, 0)
    game.make_player_move(1, 1)
    game.make_move()

    assert game.is_over() == -1

    game = TicTacToe(3)

    game.make_player_move(0, 1)
    game.make_player_move(1, 0)
    game.make_player_move(1, 2)
    game.make_player_move(2, 1)
    game.make_move()
    game.make_move()
    game.make_move()
    game.make_move()
    game.make_move()

    assert game.is_over() == 1

    game = TicTacToe(3)

    game.make_player_move(0, 1)
    game.make_player_move(1, 0)
    game.make_player_move(1, 1)
    game.make_player_move(2, 2)
    game.make_move()
    game.make_move()
    game.make_move()
    game.make_move()
    game.make_move()

    assert game.is_over() == 2