# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
 
from logic import Game, Human, Bot

if __name__ == '__main__':
    game_mode = input("Enter game mode (1 for single player, 2 for two players): ")

    if game_mode == '1':
        game = Game(Human(), Bot())
    elif game_mode == '2':
        game = Game(Human(), Human())
    else:
        print("Invalid game mode. Exiting.")
        exit()

    game.run()