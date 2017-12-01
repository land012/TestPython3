# coding: utf-8

import unittest

class ListDemo2(unittest.TestCase):

    @staticmethod
    def test1():
        """使用 list 定义 list"""
        l1 = list([1, 2, 3])
        print(l1)

        # TypeError: list() takes at most 1 argument (3 given)
        # l2 = list(2, 3, 4)
        # print(l2)

    @staticmethod
    def test2():
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l3 = list()
        l3.append(l1)
        l3.append(l2)
        print(l3)  # [[1, 2, 3], [4, 5, 6]]