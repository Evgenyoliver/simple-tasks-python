import unittest
from polka import *
class PolkaTest(unittest.TestCase):
    def test_polka_notation(self):
        self.assertEqual(polka_notation("5 8 3 + *"), 55)
        self.assertEqual(polka_notation("5 3 18 / *"), 30)
        self.assertEqual(polka_notation("5 5 11 10 * / *"), 110)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, polka_notation, "0 8 3 + /")

if __name__ == '__main__':
    unittest.main()
