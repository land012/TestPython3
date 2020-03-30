# coding: utf-8
"""
# Created by xudazhou at 2019/12/17

字节类型 转 十六进制
"""
import unittest
import binascii
import base64


class HexTest(unittest.TestCase):

    @staticmethod
    def test1():
        """

        :return:
        """
        s1 = b"lo"
        hex1 = binascii.b2a_hex(s1)
        print(type(hex1))  # <class 'bytes'>
        print(hex1)  # b'6c6f'
        print(binascii.hexlify(s1))  # b'6c6f'

        print(binascii.a2b_hex(hex1))  # b'lo'

    @staticmethod
    def test2():
        s2 = b'lo'
        print(type(s2))  # <class 'bytes'>

        # bytes类型 转 字节类型十六进制
        hex1 = base64.b16encode(s2)
        print(type(hex1))  # <class 'bytes'>
        print(hex1)  # b'6C6F'

        # 字节类型十六进制 转换 bytes类型
        print(base64.b16decode(hex1))  # b'lo'

        # 字节类型十六进制 转 字符类型十六进制
        hex1_str = hex1.decode(encoding="ascii")
        print(type(hex1_str))  # <class 'str'>
        print(hex1_str)  # 6C6F

        # 字符类型十六进制 转 bytes类型
        by2 = bytes.fromhex(hex1_str)
        print(by2)  # b'lo'
