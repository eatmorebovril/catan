import Player

class Game:
    def __init__(self):
        self.players = []

        self.startGame()


    def __str__(self):
        return f""

    def __repr__(self):
        return self.__str__()

    def startGame(self):
        """
        Starts the game by initializing players, resources, and the game board.
        """

        self.players = [Player.Player(i) for i in range(4)]

new_game = Game()
print(new_game.players[0].settlementCount)