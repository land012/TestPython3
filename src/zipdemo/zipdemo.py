# coding: utf-8

import unittest
import numpy as np


class ZipDemo(unittest.TestCase):

    @staticmethod
    def test1():
        x = [1, 2 ,3]
        y = [4, 5, 6]
        z1 = zip(x, y)
        print(z1)  # <zip object at 0x00000000031B9F88>
        # 解压
        print(*z1)  # (1, 4) (2, 5) (3, 6)

    @staticmethod
    def test1_1():
        x = [1, 4]
        y = [2, 5]
        z = [3, 6]
        z1 = zip(x, y, z)
        print(list(z1))  # [(1, 2, 3), (4, 5, 6)]

    @staticmethod
    def test2():
        """解压/遍历"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        z1 = zip(x, y)
        print(z1)  # <zip object at 0x00000000031B9F88>
        uz1 = zip(*z1)
        print(uz1)  # <zip object at 0x00000000031B9F88>
        print(*uz1)  # (1, 2, 3) (4, 5, 6)

    @staticmethod
    def test2_1():
        """解压/遍历"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        z1 = zip(x, y)
        print(z1)  # <zip object at 0x00000000031B9F88>
        x1, y1 = zip(*z1)
        print(x1)  # (1, 2, 3)
        print(y1)  # (4, 5, 6)

    @staticmethod
    def test2_2():
        """解压/遍历"""
        x = [1, 2, 3]
        y = [4, 5, 6]
        z1, z2, z3 = zip(x, y)
        print(type(z1))  # <class 'tuple'>
        print(z1)  # (1, 4)
        print(z2)  # (2, 5)
        print(z3)  # (3, 6)

    @staticmethod
    def test_count():
        """解压 zip"""
        arr1 = np.array([1, 2, 1, 3, 4, 5])
        uniq = np.unique(arr1, return_counts=True)
        print(uniq)  # (array([1, 2, 3, 4, 5]), array([2, 1, 1, 1, 1], dtype=int64))
        l_zip = zip(*uniq)
        print(l_zip)  # <zip object at 0x00000000030D7148>
        # 下面这两句只能存在一个，会遍历 l_zip
        print(*l_zip)  # (1, 2) (2, 1) (3, 1) (4, 1) (5, 1)
        # print(list(l_zip))
        # print(dict(*l_zip))  # {1: 2, 2: 1, 3: 1, 4: 1, 5: 1}

    @staticmethod
    def test_count3():
        """解压 zip"""
        arr1 = np.array([1, 2, 1, 3, 4, 5])
        uniq = np.unique(arr1, return_counts=True)
        print(uniq)  # (array([1, 2, 3, 4, 5]), array([2, 1, 1, 1, 1], dtype=int64))
        l_zip = zip(*uniq)
        print(l_zip)  # <zip object at 0x00000000030D7148>
        print(list(l_zip))  # [(1, 2), (2, 1), (3, 1), (4, 1), (5, 1)]

    @staticmethod
    def test_count2():
        arr1 = np.array([1, 9, 1, 1, 4, 5])
        uniq = np.unique(arr1, return_counts=True)
        print(uniq)  # (array([1, 4, 5, 9]), array([3, 1, 1, 1], dtype=int64))
        l_zip = zip(*uniq)
        print(l_zip)  # <zip object at 0x00000000030D7148>
        print(dict(l_zip))  # {1: 2, 2: 1, 3: 1, 4: 1, 5: 1}
