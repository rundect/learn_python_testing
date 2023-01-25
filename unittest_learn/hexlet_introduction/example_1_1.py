
"""
Мир Python: тестирование с помощью unittest
https://ru.hexlet.io/courses/advanced_python/lessons/python_testing_unittest/theory_unit
"""
# -*- encoding: utf-8 -*-


import unittest


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()
