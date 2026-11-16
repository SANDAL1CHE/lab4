import unittest
import math
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        # Проверка площади круга с нулевым радиусом
        res = area(0)
        self.assertEqual(res, 0)

    def test_unit_area(self):
        # Проверка площади круга с радиусом 1
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_zero_perimeter(self):
        # Проверка длины окружности при нулевом радиусе
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_unit_perimeter(self):
        # Проверка длины окружности с радиусом 1
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)

if __name__ == '__main__':
    unittest.main()