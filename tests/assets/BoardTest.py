from assets.Board.Tile import Tile
from constants.constants import DESERT, OUTER_TILE_POSITIONS, INNER_TILE_POSITIONS, CENTRE_TILE_POSITION
from tests.constants import STANDARD_TILE_POSITIONS
from tests.helpers import makeBoardNoSetup
from utils.FunctionUtils import rotateList
from unittest.mock import patch
import copy
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = makeBoardNoSetup()

    def testShuffleTilesRandomisesDecks(self) -> None:
        original_tile_deck = copy.deepcopy(self.board.tile_deck)
        original_port_deck = copy.deepcopy(self.board.port_deck)

        self.board.shuffleTiles()

        # The decks should have the same elements
        self.assertCountEqual(self.board.tile_deck, original_tile_deck)
        self.assertCountEqual(self.board.port_deck, original_port_deck)

    def testDealTilesPopulatesBoardWithCorrectTilesAndNumbers(self) -> None:
        board = makeBoardNoSetup()
        board.tile_positions = STANDARD_TILE_POSITIONS

        board.dealTiles()

        # Build expected adjusted numbers (insert None at desert index)
        adjusted_numbers = list(board.tile_numbers)
        desert_index = board.tile_deck.index(DESERT)
        adjusted_numbers.insert(desert_index, None)

        for i, (row, col) in enumerate(board.tile_positions):
            tile = board.board[row][col]
            self.assertIsInstance(tile, Tile)
            self.assertEqual(tile.resource, board.tile_deck[i])
            self.assertEqual(tile.number, adjusted_numbers[i])

        # Desert specific checks
        d_row, d_col = board.tile_positions[desert_index]
        self.assertEqual(board.board[d_row][d_col].resource, DESERT)
        self.assertIsNone(board.board[d_row][d_col].number)

    def testDealTilesDesertNumberNoneAfterShuffleChange(self):
        board = makeBoardNoSetup()
        board.tile_positions = STANDARD_TILE_POSITIONS

        # Simulate a shuffle that reverses the deck (desert moves position)
        board.tile_deck.reverse()

        board.dealTiles()

        desert_index = board.tile_deck.index(DESERT)
        d_row, d_col = board.tile_positions[desert_index]
        desert_tile = board.board[d_row][d_col]
        self.assertIsNone(desert_tile.number)
        self.assertEqual(desert_tile.resource, DESERT)

        # Ensure only one tile got a None number
        none_count = sum(
            1 for (r, c) in board.tile_positions
            if board.board[r][c].number is None
        )
        self.assertEqual(none_count, 1)

    def testPrepareTilePositionsProduces19UniqueValidCoordinates(self):
        board = makeBoardNoSetup()
        with patch('assets.Board.Board.random.randint', return_value=0):
            board.prepareTilePositions()

        self.assertEqual(len(board.tile_positions), 19)
        self.assertEqual(len(set(board.tile_positions)), 19)

        # All coordinates must be valid indices into board structure
        for r, c in board.tile_positions:
            self.assertGreaterEqual(r, 0)
            self.assertLess(r, len(board.board))
            self.assertGreaterEqual(c, 0)
            self.assertLess(c, len(board.board[r]))

        # Centre position should be last
        self.assertEqual(board.tile_positions[-1], CENTRE_TILE_POSITION[0])

    def testPrepareTilePositionsRotationMatchesOffset(self):
        for offset in range(6):
            board = makeBoardNoSetup()
            with patch('assets.Board.Board.random.randint', return_value=offset):
                board.prepareTilePositions()

            expected_outer = sum(rotateList(OUTER_TILE_POSITIONS, offset), [])
            expected_inner = rotateList(INNER_TILE_POSITIONS, offset)
            expected = expected_outer + expected_inner + CENTRE_TILE_POSITION
            self.assertEqual(board.tile_positions, expected, msg=f"Offset {offset} failed")

    def testPrepareTilePositionsDifferentOffsetsChangeOrdering(self):
        board_a = makeBoardNoSetup()
        board_b = makeBoardNoSetup()
        with patch('assets.Board.Board.random.randint', return_value=0):
            board_a.prepareTilePositions()
        with patch('assets.Board.Board.random.randint', return_value=3):
            board_b.prepareTilePositions()

        self.assertNotEqual(board_a.tile_positions, board_b.tile_positions)
        # Sets are equal because it's a rotation of groups
        self.assertEqual(set(board_a.tile_positions), set(board_b.tile_positions))


if __name__ == "__main__":
    unittest.main()
