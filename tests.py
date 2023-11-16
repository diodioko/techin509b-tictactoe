import unittest
from unittest.mock import patch
from logic import Board, Game, Human, Bot


class TestTicTacToe(unittest.TestCase):

    def test_make_empty_board(self):
        board = Board()
        empty_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(board.get_board(), empty_board)

    def test_other_player(self):
        playerX = Human()
        playerO = Bot()
        game = Game(playerX, playerO)

        with patch('builtins.input', side_effect=['0', '0']):
            move = playerX.get_move(game._board.get_board())
        self.assertEqual(move, (0, 0))

    def test_check_winner(self):
        # Assuming that the get_winner() method works correctly, this test checks if it is correctly identified
        # when a player has won.

        # Create a winning board for player 'X'
        winning_board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', ' ', 'O']
        ]
        game = Game(Human(), Human())
        game._board._board = winning_board
        winner = game.get_winner()
        self.assertEqual(winner, 'X')

    def test_get_winner(self):
        # Assuming that the get_winner() method works correctly, this test checks if it correctly identifies
        # when there is no winner (game still in progress).

        # Create a board with no winner yet
        in_progress_board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            [' ', ' ', ' ']
        ]
        game = Game(Human(), Human())
        game._board._board = in_progress_board
        winner = game.get_winner()
        self.assertIsNone(winner)

    def test_assign_bot(self):
        # Assuming that the Bot class is working correctly, this test checks if a Bot instance is correctly assigned
        game = Game(Human(), Bot())
        self.assertIsInstance(game._playerO, Bot)



if __name__ == '__main__':
    unittest.main()