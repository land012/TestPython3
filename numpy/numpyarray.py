# coding: utf-8

import unittest
import numpy as np


class NumpyArrayTest(unittest.TestCase):

    @staticmethod
    def test1():
        arr1 = np.array([1, 2, 3, 1, 2, 1])
        print(arr1)

    @staticmethod
    def test2():
        arr2 = np.array(["a", "b", "c"])
        print(arr2)