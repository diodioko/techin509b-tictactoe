# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None if there's no winner."""
    for player in ['X', 'O']:
        # Check rows
        for row in board:
            if all(cell == player for cell in row):
                return player

        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return player

        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player

    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'
    else:
        raise ValueError("Invalid player character")