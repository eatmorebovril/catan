import random
from exceptions.EmptyHandError import EmptyHandError

class Player:
    def __init__(self, turn_order, name=None):
        self.turn_order = turn_order
        self.name = name if name is not None else "Player " + str(self.turn_order + 1)
        self.hand = []
        self.isTurn = False

        self.settlementCount = 5
        self.cityCount = 4
        self.roadCount = 15

        self.longestRoad = False
        self.largestArmy = False

        self.maxRoadLength = 0
        self.armySize = 0

        self.developmentCards = {
            "knight": 0,
            "victory_point": 0,
            "road_building": 0,
            "year_of_plenty": 0,
            "monopoly": 0
        }

        self.victoryPoints = 0

    def __str__(self):
        return (
            f"Player Name: {self.name}\n"
            f"  Turn Order: {self.turn_order}\n"
            f"  Hand Size: {len(self.hand)}\n"
            f"  Is Turn: {self.isTurn}\n"
        )

    def __repr__(self):
        return self.__str__()

    def startTurn(self):
        self.isTurn = True

    def endTurn(self):
        self.isTurn = False

    def handSize(self):
        return len(self.hand)

    def addToHand(self, resource):
        self.hand.append(resource)

    def removeFromHandRandomly(self):
        if self.handSize() == 0:
            raise EmptyHandError(self)

        random_index = random.randint(0, len(self.hand) - 1)
        return self.hand.pop(random_index)

    def removeFromHandByIndex(self, index):
        if self.handSize() == 0:
            raise EmptyHandError(self)

        if index < 0 or index >= self.handSize():
            raise IndexError("Index out of range for hand.")

        return self.hand.pop(index)

    def removeFromHandByResource(self, resource):
        if resource not in self.hand:
            return None

        self.hand.remove(resource)
        return resource

    def useKnight(self):
        if self.developmentCards["knight"] == 0:
            return False

        self.developmentCards["knight"] -= 1
        self.armySize += 1


# p1 = Player(0)
#
# def testFailure():
#     try:
#         p1.removeFromHandRandomly()
#     except Exception as e:
#         # print("Caught an exception:")
#         print(e)
#
# testFailure()

# print(p1.removeFromHandRandomly())