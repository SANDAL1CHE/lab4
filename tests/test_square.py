import unittest
import sys
import os

# Добавляем путь к папке src в sys.path для корректного импорта тестируемых модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        # Проверка площади квадрата с нулевой стороной
        res = area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        # Проверка площади квадрата
        res = area(5)
        self.assertEqual(res, 25)

    def test_zero_perimeter(self):
        # Проверка периметра квадрата с нулевой стороной
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_perimeter(self):
        # Проверка периметра квадрата
        res = perimeter(4)
        self.assertEqual(res, 16)

if __name__ == '__main__':
    unittest.main()