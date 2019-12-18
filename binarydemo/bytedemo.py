__author__ = 'xudazhou'

import unittest


class BytesTest(unittest.TestCase):

    @staticmethod
    def test1():
        b1 = b"hello"
        print(type(b1))  # <class 'bytes'>
        str1 = str(b1, encoding='utf-8')
        print(type(str1))  # <class 'str'>
        print(str1)

        print("================== 1 ====================")

        b2 = str1.encode(encoding='gbk')
        str2 = b2.decode(encoding='gbk')
        print(type(b2))  # <class 'bytes'>
        print(b2)  # b'hello'
        print(type(str2))  # <class 'str'>
        print(str2)  # hello

        print("================= 2 =====================")

        b3 = "中文".encode(encoding='utf-8')
        print(b3)  # b'\xe4\xb8\xad\xe6\x96\x87'
        print(b3[0])  # 228

    @staticmethod
    def test2_ljust():
        str1 = "abc"
        bytes1 = str1.encode(encoding="utf-8")
        print(bytes1)  # b'abc'

        bytes2 = bytes1.ljust(4)
        print(bytes2)  # b'abc '
        print(bytes1[:-1])

    @staticmethod
    def test3_1():
        str1 = "ｂ"
        byte1 = str1.encode(encoding="utf-8")
        print(byte1)  # b'\xef\xbd\x82'
