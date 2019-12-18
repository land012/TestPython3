import struct
import sys
import unittest

__author__ = 'xudazhou'


class StructDemo(unittest.TestCase):

    @staticmethod
    def test1():
        i1 = 5
        # int 转 字节数组
        s1 = struct.pack('i', i1)
        print(type(s1))  # <class 'bytes'>
        print(len(s1))  # 4
        print(s1) # b'\x05\x00\x00\x00'
        # TypeError: must be str, not bytes
        #sys.stdout.write(s1)

        s2 = struct.pack('>i', i1)
        print(s2) # b'\x00\x00\x00\x05'

        # 字节数组 转 int
        i1_1 = struct.unpack('>i', s2)[0]
        print(i1_1)  # 5

    @staticmethod
    def test2():
        # 补码表示
        # b'\x86'
        print(struct.pack("b", -122))  # b'\x86'
        print(struct.unpack("B",  b'\x86')[0])  # 134

        print(struct.pack("b", -120))  # b'\x88'
        print(struct.unpack("B", b'\x88')[0])  # 136

        print(struct.pack("b", -1))  # b'\xff'
        print(struct.unpack("B", b'\xff')[0])  # 255

        print(struct.unpack("b", b'\x80')[0])  # -128
        print(struct.unpack("b", b'\x00')[0])  # 0
        print(struct.unpack("b", b'\x71')[0])  # 113

    @staticmethod
    def test3():
        # 补码表示
        # b'\x86'
        print(struct.pack("!i", -307))  # b'\x86'