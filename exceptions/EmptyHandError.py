class EmptyHandError(Exception):
    """
    Exception raised when a player attempts to remove a resource from an empty hand.
    """

    def __init__(self, player):
        self.player = player
        self.playerName = player.name if player.name else "Unknown Player"
        self.message = f"{self.playerName}'s hand is empty and a resource cannot be removed."

        super().__init__(self.message)

    def __str__(self):
        return self.message