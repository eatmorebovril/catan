class Tile:
    def __init__(self, resource: str, position: tuple, number: int = None):
        self.resource = resource
        self.position = position
        self.number = number
        self.adjacentSettlementPositions = []

        self.has_robber = number is None

    def __str__(self):
        number = f"({self.number}) " if self.number is not None else ""
        return f"{number}{self.resource}"

    def __repr__(self):
        number = f"({self.number}) " if self.number is not None else ""
        return f"{number}{self.resource} tile at {self.position}"