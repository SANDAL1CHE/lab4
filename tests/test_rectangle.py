import unittest
import sys
import os

# Добавляем путь к папке src в sys.path для корректного импорта тестируемых модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        # Проверка умножения на ноль
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        # Проверка площади для равных сторон 
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_normal_area(self):
        # Проверка площади
        res = area(5, 8)
        self.assertEqual(res, 40)

    def test_normal_perimeter(self):
        # Проверка периметра
        res = perimeter(5, 8)
        self.assertEqual(res, 26)

    def test_zero_perimeter(self):
        # Проверка периметра при нулевых сторонах
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()