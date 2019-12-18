# coding: utf-8

__author__ = 'xudazhou'

import math
import unittest

class MathDemo(unittest.TestCase):
    @staticmethod
    def test1():
        i = 1
        i += 1
        print(i)  # 2

        print(3 / 2)  # 1.5
        print(3 // 2)  # 1

    @staticmethod
    def test_ceil():
        print(math.ceil(1.1))  # 2
        print(math.ceil(1.5))  # 2
        print(math.ceil(2))  # 2

    @staticmethod
    def test_log():
        print(math.log(9, 3))

    @staticmethod
    def test_pow():
        print(2 ** -3)
        print(1 / 2 ** 3)
        print(math.pow(2, 15))  # 32768.0
        print(math.pow(2, 16))  # 65536.0
        print(math.pow(2, 32))  # 4294967296.0


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MathDemo('test_log'))
    suite.addTest(MathDemo('test_pow'))

    unittest.TextTestRunner(verbosity=2).run(suite)
