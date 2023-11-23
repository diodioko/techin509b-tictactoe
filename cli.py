# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
 
from logic import Game, Human, Bot
import os
import csv

if not os.path.exists("logs"):
    os.makedirs("logs")

if not os.path.exists("logs/database.csv"):
    with open("logs/database.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Winner'])

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

    # Report on game statistics
    with open("logs/database.csv", mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    total_games = len(data) - 1  # Subtracting header row
    total_wins_X = data.count(['X'])
    total_wins_O = data.count(['O'])
    total_draws = data.count(['Draw'])