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
        writer.writerow(['Winner', 'FirstPlayer', 'FirstPlayerMove'])

if __name__ == '__main__':
    total_games = 0
    total_wins_X = 0
    total_wins_O = 0
    total_draws = 0

    while True:
        first_player = input("Do you want to play as X or O? ").upper()
        if first_player not in ['X', 'O']:
            print("Invalid choice. Please enter either 'X' or 'O'.")
            continue

        game_mode = input("Do you want to play against a human (1) or a bot (2)? ")
        if game_mode == '1':
            second_player = 'O' if first_player == 'X' else 'X'
            game = Game(Human(), Human(), first_player)
        elif game_mode == '2':
            second_player = 'O' if first_player == 'X' else 'X'
            game = Game(Human(), Bot(), first_player)
        else:
            print("Invalid game mode. Try again.")
            continue

        total_games += 1
        game.run(total_games)

        # Update statistics
        with open("logs/database.csv", mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        total_wins_X += data.count(['X', first_player, str(first_player) + str((0, 0))])
        total_wins_O += data.count(['O', first_player, str(first_player) + str((0, 0))])
        total_draws += data.count(['Draw', first_player, str(first_player) + str((0, 0))])

    print("Overall Statistics:")
    print(f"Total Games: {total_games}")
    print(f"Total Wins for X: {total_wins_X}")
    print(f"Total Wins for O: {total_wins_O}")
    print(f"Total Draws: {total_draws}")