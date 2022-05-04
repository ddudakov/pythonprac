import unittest
from prog import solveSquare

class TestSq(unittest.TestCase):

    def test_pos_d(self):
        self.assertEqual(solveSquare(1, -3, 2), (1, 2))

    def test_neg_d(self):
        self.assertEqual(solveSquare(1, 1, 1), None)
        
    def test_zero_d(self):
        self.assertEqual(solveSquare(1, -4, 4), (2, 2))
