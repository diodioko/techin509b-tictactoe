# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import logging
from logic import TicTacToe

logging.basicConfig(
    filename='logs/game_records.log',
    level=logging.INFO
)

def print_board(board):
    for row in board:
        print(" | ".join([cell or ' ' for cell in row]))
        print("---------")

def play_game_single_player():
    game = TicTacToe()
    while game.winner is None:
        print("Current board:")
        print_board(game.board)
        print(f"It's {game.current_player}'s turn.")

        if game.current_player == 'X':
            while True:
                try:
                    row = int(input("Enter the row (0, 1, or 2): "))
                    col = int(input("Enter the column (0, 1, or 2): "))
                    game.make_move(row, col)
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")
        else:  # Bot's turn
            # Add your bot logic here (e.g., random moves)
            # For now, let's make random moves for the bot
            import random
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if game.board[row][col] is None:
                    game.make_move(row, col)
                    break

        winner = game.winner
        if winner == 'X' or winner == 'O':
            print_board(game.board)
            print(f"{winner} wins!")
            logging.info(f'{winner} won')
        elif winner == 'Tie':
            print_board(game.board)
            print("It's a tie!")
            logging.info('Tie')

def play_game_two_players():
    game = TicTacToe()
    while game.winner is None:
        print("Current board:")
        print_board(game.board)
        print(f"It's {game.current_player}'s turn.")
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                game.make_move(row, col)
                break
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        winner = game.winner
        if winner == 'X' or winner == 'O':
            print_board(game.board)
            print(f"{winner} wins!")
            logging.info(f'{winner} won')
        elif winner == 'Tie':
            print_board(game.board)
            print("It's a tie!")
            logging.info('Tie')

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    print("Choose the game mode:")
    print("1. Single Player (against a bot)")
    print("2. Two Players")
    
    while True:
        try:
            choice = int(input("Enter 1 or 2: "))
            if choice in (1, 2):
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

    if choice == 1:
        play_game_single_player()
    else:
        play_game_two_players()