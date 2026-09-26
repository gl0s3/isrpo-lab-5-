import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(0), 0)
    def test_unit_mul(self):
        self.assertEqual(area(1), math.pi)
    def test_square_mul(self):
        self.assertAlmostEqual(area(3), 9 * math.pi)
    def test_zero_per(self):
        self.assertEqual(perimeter(0), 0)
    def test_unit_per(self):
        self.assertEqual(perimeter(1), 2 * math.pi)
    def test_bignumbers_per(self):
        self.assertEqual(perimeter(13), 26 * math.pi)