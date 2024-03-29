
"""
Мир Python: тестирование с помощью unittest
https://ru.hexlet.io/courses/advanced_python/lessons/python_testing_unittest/theory_unit

Приведу пример, как можно протестировать конструктор
"""
# -*- encoding: utf-8 -*-

import unittest


class MyClass(object):
    def __init__(self, foo):
        if foo != 1:
            raise ValueError("foo is not equal to 1!")


class MyClass2(object):
    def __init__(self):
        pass


class TestFoo(unittest.TestCase):
    def testInsufficientArgs(self):
        foo = 0
        self.assertRaises(ValueError, MyClass, foo)

    def testArgs(self):
        self.assertRaises(TypeError, MyClass2, ("fsa", "fds"))


if __name__ == '__main__':
    unittest.main()
