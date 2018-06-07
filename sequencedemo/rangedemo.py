import unittest

__author__ = 'xudazhou'

def fn1():
    """不包括 end"""
    l1 = range(3, 5)
    print(type(l1))  # <class 'range'>

    for i in l1:
        print(i, end=" ")  # 3 4


def fn2():
    # 指定步长
    for i in range(1, 9, 2):
        print(i, end=" ")  # 1 3 5 7


def fn3():
    for i in range(0, 0):
        print(i, end=" ")  #


def fn4():
    """默认从 0 开始"""
    for i in range(2):
        print(i, end=" ")


class RangeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        fn1()

    @staticmethod
    def test2():
        fn2()

    @staticmethod
    def test4():
        fn4()