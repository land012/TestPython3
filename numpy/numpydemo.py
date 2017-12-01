# coding: utf-8

import numpy as np
import unittest


class NumpyDemo(unittest.TestCase):

    @staticmethod
    def test1():
        """均值 方差"""
        arr1 = np.array([1, 2, 3, 4, 5])
        print(np.mean(arr1))  # 3.0
        print(np.var(arr1))  # 2.0

        arr2 = np.array([2, 2, 3, 4, 4])
        print(np.var(arr2))  # 0.8

    @staticmethod
    def test2():
        """下标从 0 开始"""
        arr1 = np.array([4, 3, 6, 2])
        print(arr1[0])  # 4

        arr1.append(3)
        print(arr1)

    @staticmethod
    def test3():
        """
        90分位
        变异值对结果有较大影响
        """
        arr1 = np.array([1, 2, 3, 4, 5])
        print(np.percentile(arr1, 90))  # 4.6
        print(np.percentile(arr1, 90, interpolation="nearest"))  # 5
        print(np.percentile(arr1, 80))  # 4.2
        print(np.percentile(arr1, 80, interpolation="nearest"))  # 4

        arr2 = np.array([1, 2, 3, 4, 10])
        print(np.percentile(arr2, 90))  # 7.6
        print(np.percentile(arr2, 90, interpolation="nearest"))  # 10
        print(np.percentile(arr2, 80))  # 5.2
        print(np.percentile(arr2, 80, interpolation="nearest"))  # 4

    @staticmethod
    def test4():
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        arr2 = arr1[:, 2]
        print(arr2)
