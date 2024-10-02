import unittest
from RPS import player

class TestRPS(unittest.TestCase):

    def test_initial_move(self):
        self.assertIn(player("", []), ["R", "P", "S"])

    def test_counter_move(self):
        self.assertEqual(player("R"), "P")  # Paper beats Rock
        self.assertEqual(player("P"), "S")  # Scissors beat Paper
        self.assertEqual(player("S"), "R")  # Rock beats Scissors

    def test_random_move(self):
        moves = [player("", []), player("R"), player("P"), player("S")]
        self.assertTrue(all(move in ["R", "P", "S"] for move in moves))

if __name__ == "__main__":
    unittest.main()
