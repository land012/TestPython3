# coding: utf-8

import unittest


class StringFormat(unittest.TestCase):

    @staticmethod
    def test_format1():
        """格式化"""
        # g
        '''
        print("%g" % 0.000454)    # 0.000454
        print("%g" % 0.0000454)   # 4.54e-05
        print("%g" % 0.00000454)  # 4.54e-06
        '''

        # dict
        # print("%(a)s %(b)s" % {"a": "小王", "b": "小李"})  # 小王 小李

    @staticmethod
    def test_format():
        d2 = 123.332345
        d1 = "%.5f" % d2
        print(type(d1))  # <class 'str'>
        print(d1)  # 123.33235

        d3 = "%*.*f" % (0, -2, d2)
        print(d3)

    @staticmethod
    def test_format2():
        print("%d %s" % 2)
