import unittest
from rectangle import area, perimeter 


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):  
        self.assertEqual(area(10, 0 ), 0) 
    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)
    def test_bignumbers_mul(self): 
        self.assertEqual(area(91321, 12321), 1125166041)
    def test_zero_per(self): 
        self.assertEqual(perimeter(10, 0), 20)
    def test_square_per(self):
        self.assertEqual(perimeter(12, 12), 48 )

