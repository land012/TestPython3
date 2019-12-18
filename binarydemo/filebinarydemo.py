import unittest
import base64
"""
"""
__author__ = 'xudazhou'


class FileBinaryTest(unittest.TestCase):

    @staticmethod
    def test1():
        f = open(r"E:\Music\_qq_cache\4983359959083398.mp4", mode="rb")
        l_bytes = f.read(4)
        print(type(l_bytes))  # <class 'bytes'>

        while len(l_bytes) > 0:
            print(len(l_bytes))
            i1 = int.from_bytes(l_bytes,byteorder="big")
            print(hex(i1))
            l_bytes = f.read(4)

    @staticmethod
    def test2():
        f = open(r"E:\Music\_qq_cache\4983359959083398.mp4", mode="rb")
        l_bytes = f.read(4)
        print(type(l_bytes))  # <class 'bytes'>

        count = 1
        while len(l_bytes) > 0 and count < 20:
            print(base64.b16encode(l_bytes).decode("ascii"))
            l_bytes = f.read(4)
            count += 1
