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

