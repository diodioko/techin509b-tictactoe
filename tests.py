import unittest
from logic import Board, Game, Human, Bot

class TestLogic(unittest.TestCase):

    def test_make_empty_board(self):
        board = Board()
        empty_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(board.get_board(), empty_board)

    def test_make_move(self):
        board = Board()
        player = 'X'
        self.assertTrue(board.make_move(0, 0, player))
        self.assertEqual(board.get_board()[0][0], player)

    def test_invalid_move(self):
        board = Board()
        player = 'O'
        # Making a valid move first
        board.make_move(1, 1, 'X')
        self.assertFalse(board.make_move(1, 1, player))  # Invalid move, cell already occupied

    def test_get_winner_rows(self):
        game = Game(Human(), Human())
        game._board.make_move(0, 0, 'X')
        game._board.make_move(0, 1, 'X')
        game._board.make_move(0, 2, 'X')
        self.assertEqual(game.get_winner(), 'X')

    def test_get_winner_columns(self):
        game = Game(Human(), Human())
        game._board.make_move(0, 0, 'O')
        game._board.make_move(1, 0, 'O')
        game._board.make_move(2, 0, 'O')
        self.assertEqual(game.get_winner(), 'O')

    def test_get_winner_diagonal(self):
        game = Game(Human(), Human())
        game._board.make_move(0, 0, 'X')
        game._board.make_move(1, 1, 'X')
        game._board.make_move(2, 2, 'X')
        self.assertEqual(game.get_winner(), 'X')

    def test_get_winner_no_winner(self):
        game = Game(Human(), Human())
        game._board.make_move(0, 0, 'O')
        game._board.make_move(1, 1, 'X')
        game._board.make_move(2, 2, 'O')
        self.assertIsNone(game.get_winner())

    # Add more tests for other functions as needed

if __name__ == '__main__':
    unittest.main()