from assets.Board.Tile import Tile
from assets.Board.Port import Port
from constants.constants import (WOOD, BRICK, SHEEP, WHEAT, ORE, DESERT, INITIAL_TILE_NUMBERS,
                                 OUTER_TILE_POSITIONS, INNER_TILE_POSITIONS, CENTRE_TILE_POSITION)
from customTypes.Board import HexGrid, TilePosition
from customTypes.constants import Resource
from utils.FunctionUtils import rotateList
import random

class Board:

    def __init__(self) -> None:
        self.players = []

        self.tile_deck: list[Resource] = [
            WOOD, WOOD, WOOD, WOOD,
            BRICK, BRICK, BRICK,
            SHEEP, SHEEP, SHEEP, SHEEP,
            WHEAT, WHEAT, WHEAT, WHEAT,
            ORE, ORE, ORE,
            DESERT
        ]

        self.port_deck: list[Port] = [
            Port(WOOD), Port(BRICK), Port(SHEEP),
            Port(WHEAT), Port(ORE), Port(),
            Port(), Port(), Port()
        ]

        self.tile_numbers: list[int | None] = INITIAL_TILE_NUMBERS

        self.tile_positions: list[TilePosition] = []
        self.board: HexGrid = [
            [None, None, None],
            [None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None],
            [None, None, None]
        ]

        self.setUpBoard()

    def __str__(self) -> str:
        return "\n".join(
            " | ".join(str(tile) if tile else "Empty" for tile in row)
            for row in self.board
        )

    def __repr__(self) -> str:
        return f"Board(players={len(self.players)}, tiles={sum(1 for row in self.board for tile in row if tile)})"

    def setUpBoard(self) -> None:
        """
        Sets up the board with tiles, resources, and initial player placements.
        """
        self.shuffleTiles()
        self.prepareTilePositions()
        self.dealTiles()
        print(self.port_deck)

        # toDo Initialise ports

    def shuffleTiles(self) -> None:
        """
        Shuffles the decks to randomize the board set-up.
        """
        random.shuffle(self.tile_deck)
        random.shuffle(self.port_deck)

    def dealTiles(self) -> None:
        """
        Deals tiles to the board positions from the shuffled tile deck.
        """
        # Pre-process the tile numbers for desert
        adjusted_numbers = list(self.tile_numbers)
        desert_index = self.tile_deck.index(DESERT)
        adjusted_numbers.insert(desert_index, None)

        # Deal tiles to positions
        for resource, position, number in zip(self.tile_deck, self.tile_positions, adjusted_numbers):
            row, col = position
            self.board[row][col] = Tile(resource, position, number)

    def prepareTilePositions(self) -> None:
        """
        Sets the positions of the tiles on the board.
        """
        starting_corner_offset = random.randint(0, 5)

        rotated_outer_positions = rotateList(OUTER_TILE_POSITIONS, starting_corner_offset)
        rotated_inner_positions = rotateList(INNER_TILE_POSITIONS, starting_corner_offset)

        self.tile_positions = sum(rotated_outer_positions, []) + rotated_inner_positions + CENTRE_TILE_POSITION

test = Board()
print(test)