import os
import pathlib
from hectorutils.byteutils import *
import unittest

__author__ = 'xudazhou'


class FileBinaryTest(unittest.TestCase):

    @staticmethod
    def test1():
        # 读二进制文件
        file1 = open("E:\\TDDOWNLOAD\\file1.dat", mode="rb")

        len1byte = file1.read(4)
        print(type(len1byte))  # <class 'bytes'>
        print(len1byte)  # b'\x00\x00\x00\x82'
        len1 = bytestoint(len1byte)
        print("len1=%d" % len1)  # len1=130

        val1byte = file1.read(len1)
        print(val1byte.decode(encoding="utf-8"))

        print("======================== 1 ==========================")

        len2byte = file1.read(4)
        len2 = bytestoint(len2byte)
        print(len2)  # 6

        val2byte = file1.read(len1)
        print(val2byte.decode(encoding="utf-8"))  # 你好
        print(str(val2byte, encoding="utf-8"))  # 你好
