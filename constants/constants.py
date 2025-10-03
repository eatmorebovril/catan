from customTypes.constants import Resource
from customTypes.Board import TilePosition

BOARD_HEIGHT = 12

MAX_PLAYERS = 4
MIN_PLAYERS = 3

WOOD: Resource = "Wood"
BRICK: Resource = "Brick"
SHEEP: Resource = "Sheep"
WHEAT: Resource = "Wheat"
ORE: Resource = "Ore"
DESERT: Resource = "Desert"

INITIAL_TILE_NUMBERS : list[int] = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

OUTER_TILE_POSITIONS: list[list[TilePosition]] = [
    [(0, 0), (1, 0)],
    [(2, 0), (3, 0)],
    [(4, 0), (4, 1)],
    [(4, 2), (3, 3)],
    [(2, 4), (1, 3)],
    [(0, 2), (0, 1)]
]

INNER_TILE_POSITIONS: list[TilePosition] = [
    (1,1), (2,1), (3,1),
    (3,2), (2,3), (1,2),
]

CENTRE_TILE_POSITION: list[TilePosition] = [(2, 2)]

NUMBER_TOKENS = (2, 3, 4, 5, 6, 8, 9, 10, 11, 12)
