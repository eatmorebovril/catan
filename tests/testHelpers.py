from assets.Board.Board import Board
from unittest.mock import patch

def makeBoardNoSetup() -> Board:
    """
    Prevent __init__ from auto-calling setUpBoard()
    """
    with patch.object(Board, "setUpBoard", lambda self: None):
        return Board()
