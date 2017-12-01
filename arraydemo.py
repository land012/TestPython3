# coding: utf-8

import array
import unittest

class ArrayDemo(unittest.TestCase):

    @staticmethod
    def test1():
        arr1 = array.array("u", 'i am tom')
        print(arr1[2])  # a
        print(arr1.itemsize)  # 2
        print(arr1.__len__())  # 8
        print(len(arr1))  # 8
