import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(0), 0)
    def test_unit_mul(self):
        self.assertEqual(area(1), 1)
    def test_square_mul(self):
        self.assertEqual(area(7), 49)
    def test_bignumbers_mul(self):
        self.assertEqual(area(91321), 8339525041)
    def test_zero_per(self):
        self.assertEqual(perimeter(0), 0)
    def test_square_per(self):
        self.assertEqual(perimeter(5), 20)
    def test_bignumbers_per(self):
        self.assertEqual(perimeter(91321), 365284)