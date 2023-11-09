# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class TicTacToe:
    def __init__(self):
        self.board = self.make_empty_board()
        self.current_player = 'X'
        self.winner = None

    @staticmethod
    def make_empty_board():
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def make_move(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.switch_player()
            self.check_winner()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        for player in ['X', 'O']:
            for row in self.board:
                if all(cell == player for cell in row):
                    self.winner = player

            for col in range(3):
                if all(self.board[row][col] == player for row in range(3)):
                    self.winner = player

            if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
                self.winner = player

        if all(cell is not None for row in self.board for cell in row):
            self.winner = 'Tie'