import unittest
from prog import solve

class TestClass(unittest.TestCase):

    def test_1(self):
        self.assertNone(solve(0,1))

    def test_2(self):
        self.assertNone(solve(0,0))

    def test_3(self):
        self.assertEqual(solve(2.0, 1.0), -0.5)
        
    def test_4(self):
        self.assertEqual(solve(0.5, -2.0), 4.0)

if __name__ == "__main__":
    unittest.main()

