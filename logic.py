# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random
import logging
import os
import csv

logging.basicConfig(filename="logs/logs.log", format='%(asctime)s %(message)s', filemode='a', force=True)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Board:
    def __init__(self):
        self._board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def make_move(self, row, col, player):
        if self._board[row][col] is None:
            self._board[row][col] = player
            return True
        return False

    def get_board(self):
        return self._board


class Game:
    def __init__(self, playerX, playerO, first_player):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = first_player

    def run(self, game_number):
        first_player_move = None

        while True:
            print("Current board:")
            self.print_board()

            print(f"It's {self._current_player}'s turn.")

            if self._current_player == 'X':
                move = self._playerX.get_move(self._board.get_board())
            else:
                move = self._playerO.get_move(self._board.get_board())

            first_player_move = move if first_player_move is None else first_player_move

            row, col = move
            if self._board.make_move(row, col, self._current_player):
                winner = self.get_winner()

                if winner:
                    print("Current board:")
                    self.print_board()
                    logger.info(f'Game {game_number}: Winner: {winner}, First Player: {self._current_player}, First Player Move: {first_player_move}')
                    self.record_winner(winner, first_player_move)
                    print(f"{winner} wins!")
                    break
                elif all(cell is not None for row in self._board.get_board() for cell in row):
                    logger.info(f'Game {game_number}: Draw, First Player: {self._current_player}, First Player Move: {first_player_move}')
                    print("Current board:")
                    self.print_board()
                    print("It's a tie!")
                    self.record_winner('Draw', first_player_move)
                    break

                self._current_player = 'O' if self._current_player == 'X' else 'X'

    def print_board(self):
        for row in self._board.get_board():
            print(" | ".join([cell or ' ' for cell in row]))
            print("---------")

    def get_winner(self):
        for player in ['X', 'O']:
            # Check rows
            for row in self._board.get_board():
                if all(cell == player for cell in row):
                    return player

            # Check columns
            for col in range(3):
                if all(row[col] == player for row in self._board.get_board()):
                    return player

            # Check diagonals
            if all(self._board.get_board()[i][i] == player for i in range(3)) or all(
                    self._board.get_board()[i][2 - i] == player for i in range(3)):
                return player

        return None

    def record_winner(self, winner, first_player_move):
        with open("logs/database.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([winner, self._current_player, str(first_player_move)])


class Human:
    def get_move(self, board):
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] is None:
                    return row, col
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")


class Bot:
    def get_move(self, board):
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(available_moves)