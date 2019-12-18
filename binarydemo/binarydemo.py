# coding: utf-8
"""
# Created by xudazhou at 2019/9/19
"""
import unittest


class BinaryDemo(unittest.TestCase):

    @staticmethod
    def test1():
        bin0 = 0b01111010  # 二进制表示法
        print(int(bin0))  # 122
        print(bin(-122))  # -0b1111010

        bin1 = 0b10000110
        print(int(bin1))  # 134

        oct1 = 0o10  # 八进制表示法
        print(int(oct1))  # 8

    @staticmethod
    def test2():
        s1 = 'a'
        o1 = ord(s1)
        print(type(o1))  # <class 'int'>
        print(o1)  # 97
        print(chr(o1))  # a
