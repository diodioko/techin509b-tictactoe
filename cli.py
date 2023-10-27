# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def print_board(board):
    for row in board:
        print(" | ".join([cell or ' ' for cell in row]))
        print("---------")

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    while winner is None:
        print("Current board:")
        print_board(board)
        
        print(f"It's {current_player}'s turn.")
        
        # Input a move from the player
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] is None:
                    board[row][col] = current_player
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
        
        # Check for a winner
        winner = get_winner(board)
        if winner:
            print(f"{winner} wins!")
        elif all(cell is not None for row in board for cell in row):
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = other_player(current_player)