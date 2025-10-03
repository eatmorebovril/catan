from assets.Board.Port import Port
from assets.Board.SettlementSpot import SettlementSpot
from assets.Board.Tile import Tile
from assets.Player import Player
from constants.constants import (WOOD, BRICK, SHEEP, WHEAT, ORE, DESERT, BOARD_HEIGHT, INITIAL_TILE_NUMBERS,
                                 OUTER_TILE_POSITIONS, INNER_TILE_POSITIONS, CENTRE_TILE_POSITION,
                                 NUMBER_TOKENS)
from customTypes.Board import HexGrid, SettlementPosition, TilePosition
from customTypes.constants import Resource
from helpers.Board import getRowLength, rotateList
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

        self.tile_positions_by_number: dict[int, list[TilePosition]] = {n: [] for n in NUMBER_TOKENS}

        self.settlement_spots_positions = {
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
            (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (9, 0), (9, 1), (9, 2), (9, 3),
            (10, 0), (10, 1), (10, 2), (10, 3),
            (11, 0), (11, 1), (11, 2)
        }

        self.settlement_spots: list[list[SettlementSpot]] = [[] for _ in range(BOARD_HEIGHT)]

        self.port_settlement_positions = [
            [(0, 0), (1, 0)],
            [(3, 0), (4, 0)],
            [(7, 0), (8, 0)],
            [(10, 0), (11, 0)],
            [(10, 2), (11, 1)],
            [(8, 4), (9, 3)],
            [(5, 5), (6, 5)],
            [(2, 3), (3, 4)],
            [(0, 1), (1, 2)]
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
        self.setUpSettlementSpots()
        self.setUpPorts()

    def shuffleTiles(self) -> None:
        """
        Shuffles the decks to randomize the board set-up.
        """
        random.shuffle(self.tile_deck)
        random.shuffle(self.port_deck)

    def prepareTilePositions(self) -> None:
        """
        Sets the positions of the tiles on the board.
        """
        starting_corner_offset = random.randint(0, 5)

        rotated_outer_positions = rotateList(OUTER_TILE_POSITIONS, starting_corner_offset)
        rotated_inner_positions = rotateList(INNER_TILE_POSITIONS, starting_corner_offset)

        self.tile_positions = sum(rotated_outer_positions, []) + rotated_inner_positions + CENTRE_TILE_POSITION

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
            if number in self.tile_positions_by_number:
                self.tile_positions_by_number[number].append(position)

    def setUpSettlementSpots(self) -> None:
        """
        Initialises settlement spots on the board.
        """
        # toDo write tests for this
        for row_index in range(BOARD_HEIGHT):
            for col_index in range(getRowLength(row_index)):
                self.settlement_spots[row_index].append(
                    SettlementSpot((row_index, col_index))
                )

    def setUpPorts(self) -> None:
        """
        Assigns ports to specified settlement spots.
        """
        # toDo write tests for this
        for pair in self.port_settlement_positions:
            port = self.port_deck.pop()
            for position in pair:
                row, col = position
                spot = self.settlement_spots[row][col]
                spot.setAdjacentPort(port)

    def buildSettlement(self, player: Player, position: SettlementPosition) -> bool:
        """
        Build a settlement for a player at a given position.
        """
        # toDo write tests for this
        row, col = position
        if not (0 <= row < BOARD_HEIGHT and 0 <= col < len(self.settlement_spots[row])):
            return False

        settlement_spot = self.settlement_spots[row][col]

        if not settlement_spot.is_settable:
            return False

        for adj_row, adj_col in settlement_spot.adjacent_settlement_positions:
            self.settlement_spots[adj_row][adj_col].is_settable = False

        settlement_spot.settlementBuilt(player)
        return True

# For testing purposes
if __name__ == "__main__":
    test = Board()
    print(test)
    print(test.settlement_spots)
