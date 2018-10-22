# coding:utf-8

import sys
import io
from hectorutils.byteutils import *

__author__ = 'xudazhou'

"""
f = io.BufferedReader(file1)
len4 = f.read(4)
print(len4)
"""

# print(sys.stdin.readline())  # 等待输入

io1 = io.BufferedReader(open("E:\\TDDOWNLOAD\\file1.dat", mode="rb"))
len1byte = io1.read1(4)
print(type(len1byte))  # <class 'bytes'>
len1 = bytestoint(len1byte)
print("len1=%d" % len1)  # len1=130
val1byte = io1.read1(len1)
print(val1byte.decode(encoding="utf-8"))
print(str(val1byte, encoding="utf-8"))
