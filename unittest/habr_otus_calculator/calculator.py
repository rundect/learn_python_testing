
"""
Юнит-тесты на Python: Быстрый старт
https://habr.com/ru/company/otus/blog/481806/
"""


# A simple calculator
class Calculator:
    # empty constructor
    def __init__(self):
        pass

    # add method - given two numbers, return the addition
    def add(self, x1, x2):
        return x1 + x2

    # multiply method - given two numbers, return the
    # multiplication of the two
    def multiply(self, x1, x2):
        return x1 * x2

    # subtract method - given two numbers, return the value
    # of first value minus the second
    def subtract(self, x1, x2):
        return x1 - x2

    # divide method - given two numbers, return the value
    # of first value divided by the second
    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2


# a = Calculator(1, 2)
# a.add(4, 5)
# print(Calculator.add())
