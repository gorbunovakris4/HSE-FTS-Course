from Board import Board
from TicTacToe import TicTacToe
from Minimax import max_depth
import Minimax

def aks_size():
    print('Please, provide the N x N field size')
    print('N: ', end='')
    size = int(input())
    print(f'OK, we play on {size} by {size} field!')
    return size

def ask_move():
    print('Please, provide your move')
    print('x: ', end='')
    x = int(input())
    print('y: ', end='')
    y = int(input())

    return x - 1, y - 1

def check_game_over(game):
    over = game.is_over()

    if over >= 0:
        print("Game is over")

        match over:
            case 0:
                print("You win!")
            case 1:
                print("You lose(")
            case 2:
                print("It's a draw!")

        return 1
    
    return 0

def play():
    size = aks_size()
    game = TicTacToe(size)
    Minimax.MAX_DEPTH = max_depth(size)
    game.board.print()

    while True:

        # player's move
        while True:
            (i, j) = ask_move()
            if game.board.set(i, j):
                break

        game.board.print()

        if check_game_over(game):
            return

        game.make_move()

        game.board.print()

        if check_game_over(game):
            return

play()
