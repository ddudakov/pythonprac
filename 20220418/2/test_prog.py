import unittest
from unittest.mock import MagicMock, patch
from prog import solve, SquareIO

class TestSqEq(unittest.TestCase):

    def test_1(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, -4, 3])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 3)

    def test_2(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, -2, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 1)

    def test_3(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [1, 1, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == None

   def test_4(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, -1, 1])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == (1, 1)

	def test_5(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 7])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == None

    def test_6(self):
        SquareIO.inputCoeff = MagicMock(side_effect = [0, 0, 0])
        SquareIO.printResult = MagicMock()
        solve()
        result = SquareIO.printResult.call_args.args[0]
        assert result == 'any value'
