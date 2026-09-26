import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(4, 0), 0)
    def test_unit_mul(self):
        self.assertEqual(area(2, 1), 1)
    def test_square_mul(self):
        self.assertEqual(area(4, 12), 24)
    def test_bignumbers_mul(self):
        self.assertEqual(area(100000, 2), 100000)
    def test_zero_per(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
    def test_square_per(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
    def test_bignumbers_per(self):
        self.assertEqual(perimeter(100000, 200000, 300000), 600000)