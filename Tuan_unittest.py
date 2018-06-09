import unittest
from calculator import Caculator


class Testing(unittest.TestCase):
    cal = Caculator()

    def test_addition(self):
        self.assertEqual((4), self.cal.add(2, 2))
        self.assertEqual(10.1, self.cal.add(1, 9.1))
        self.assertEqual(0, self.cal.add(0, 0))

    def test_minus(self):
        self.assertEqual(0, self.cal.minus(2, 2))
        self.assertEqual(2, self.cal.minus(10, 8))
        self.assertEqual(-1, self.cal.minus(0, 1))

    def test_multiple(self):
        self.assertEqual(0, self.cal.multiple(0, 1000000))
        self.assertEqual(30, self.cal.multiple(5, 6))
        self.assertEqual(-10, self.cal.multiple(-2, 5))

    def test_division(self):
        self.assertEqual(1, self.cal.divide(2, 2))
        self.assertEqual(0, self.cal.divide(0, 8.8))
        self.assertEqual(5, self.cal.divide(30, 6))
        with self.assertRaises(ZeroDivisionError):
            self.cal.divide(3, 0)

if __name__ == "__main__":
    unittest.main()
