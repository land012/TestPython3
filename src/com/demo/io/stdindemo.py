# coding:utf-8
__author__ = 'xudazhou'

import sys
import io

"""
# 等待输入，输入后，回车，按字符处理
str1 = sys.stdin.read(4)  # abcd
print(len(str1))  # 4
print(str1)  # abcd
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])

bytearr = str1.encode("utf-8")
print(len(bytearr)) # 4
print(bytearr[0])  # 97 字符ascii码的十进制表示
"""

"""
print(sys.__stdin__)  # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
print(sys.stdin)      # <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
print(sys.stdout)     # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
print(sys.stderr)     # <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>

print(sys.stdin.buffer)  # <_io.BufferedReader name='<stdin>'>
print(sys.stdout.buffer) # <_io.FileIO name='<stdout>' mode='wb'>
print(sys.stdin.encoding)  # UTF-8
print(print)  # <built-in function print>
"""

"""
byte1 = sys.stdin.buffer.read(1)
print(byte1)  # b'1'
str1 = byte1.decode(encoding="utf-8")
print(str1)  # 1
print(str1.encode(encoding="utf-8"))
"""
