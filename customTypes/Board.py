from assets.Board.Tile import Tile

BoardRow = list[Tile | None]
HexGrid = list[BoardRow]

TilePosition = tuple[int, int]
