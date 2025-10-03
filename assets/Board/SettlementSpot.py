from assets.Board.Port import Port
from assets.Player import Player
from constants.constants import BOARD_HEIGHT
from customTypes.Board import SettlementPosition
from helpers.Board import inBoardRange

class SettlementSpot:
    def __init__(self, position: SettlementPosition):
        self.position: SettlementPosition = position
        self.adjacent_settlement_positions: list[SettlementPosition] = self.getAdjacentSettlementPositions()
        self.adjacent_port: Port | None = None
        self.is_settled: bool = False
        self.is_settable: bool = True
        self.owner: Player | None = None

    def __repr__(self):
        occupier = self.owner.name + "'s" if self.owner else "Empty"
        return f"{occupier} SettlementSpot {self.position}" + (f", {self.adjacent_port}" if self.adjacent_port else "")

    def getAdjacentSettlementPositions(self) -> list[SettlementPosition]:
        row_index = self.position[0]
        col_index = self.position[1]

        direction = -1 if row_index < BOARD_HEIGHT // 2 else 1

        candidates = [
            (row_index - 1, col_index),
            (row_index + 1, col_index),
            (row_index - 1, col_index + direction) if row_index % 2 else (row_index + 1, col_index - direction)
        ]

        return [pos for pos in candidates if inBoardRange(pos)]

    def setAdjacentPort(self, port: Port):
        self.adjacent_port = port

    def settlementBuilt(self, player):
        self.is_settled = True
        self.owner = player
        self.is_settable = False

if __name__ == "__main__":
    test = SettlementSpot((11,2))
    print(test)
    print(test.adjacent_settlement_positions)
