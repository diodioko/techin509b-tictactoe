# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        winner = 'X'  # FIXME
 

from logic import make_empty_board, check_winner, print_board

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    while winner is None:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Input a move from the player
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as integers.")

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            winner = current_player
            break
        # Check if the board is full (a draw)
        elif all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            winner = 'Draw'
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'
