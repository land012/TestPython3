# coding: utf-8
"""
# Created by xudazhou at 2019/12/17
"""
import unittest
import binascii
import base64


class HexTest(unittest.TestCase):

    @staticmethod
    def test1():
        s1 = b"lo"
        hex1 = binascii.b2a_hex(s1)
        print(type(hex1))  # <class 'bytes'>
        print(hex1)  # b'6c6f'
        print(binascii.a2b_hex(hex1))  # b'lo'

    @staticmethod
    def test2():
        s2 = b'lo'
        print(type(s2))  # <class 'bytes'>
        hex1 = base64.b16encode(s2)
        print(type(hex1))  # <class 'bytes'>
        print(hex1)  # b'6C6F'

        print(base64.b16decode(hex1))  # b'lo'

        hex1_str = hex1.decode(encoding="ascii")
        print(type(hex1_str))  # <class 'str'>
        print(hex1_str)  # 6C6F
