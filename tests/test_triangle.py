import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        # Проверка площади треугольника с нулевой высотой
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        # Проверка площади треугольника по основанию и высоте
        res = area(10, 5)
        self.assertEqual(res, 25.0)

    def test_normal_perimeter(self):
        # Проверка периметра треугольника по трем сторонам
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        # Проверка периметра с нулевыми сторонами
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()