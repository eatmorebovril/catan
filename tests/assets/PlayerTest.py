import unittest
from assets.Player import Player
from exceptions.EmptyHandError import EmptyHandError

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(0, "TestPlayer")

    def testInitialHandEmpty(self):
        self.assertEqual(self.player.handSize(), 0)

    def testStartTurn(self):
        self.player.startTurn()
        self.assertTrue(self.player.isTurn)

    def testEndTurn(self):
        self.player.endTurn()
        self.assertFalse(self.player.isTurn)

    def testAddToHand(self):
        resource = "wood"

        self.player.addToHand(resource)
        self.assertIn(resource, self.player.hand)

    def testRemoveFromHandRandomlyEmpty(self):
        with self.assertRaises(EmptyHandError):
            self.player.removeFromHandRandomly()

    def testRemoveFromHandByIndexSuccess(self):
        wood = "wood"

        self.player.addToHand("stone")
        self.player.addToHand(wood)

        index_to_remove = 1
        removed = self.player.removeFromHandByIndex(index_to_remove)

        self.assertEqual(removed, wood)
        self.assertNotIn(wood, self.player.hand)

    def testRemoveFromHandByIndexEmpty(self):
        with self.assertRaises(EmptyHandError):
            self.player.removeFromHandByIndex(0)

    def testRemoveFromHandByIndexOutOfRange(self):
        self.player.addToHand("stone")

        with self.assertRaises(IndexError):
            self.player.removeFromHandByIndex(1)

    def testRemoveFromHandByResource(self):
        brick = "brick"

        self.player.addToHand(brick)
        removed = self.player.removeFromHandByResource(brick)

        self.assertEqual(removed, brick)
        self.assertNotIn(brick, self.player.hand)

if __name__ == "__main__":
    unittest.main()