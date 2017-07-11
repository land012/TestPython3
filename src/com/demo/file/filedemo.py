import os
import pathlib
from hectorutils.byteutils import *

__author__ = 'xudazhou'

"""
file1 = file("E:\TDDOWNLOAD\helloworld.txt", "r")
print(file1.readline())
"""

# 一次读整个文件
"""
file2 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
print(file2.read())
"""

# 读一行
'''
file2 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
print(file2.readline())
file2.close()
'''

# 读取文件所有内容的方式1
'''
file3 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
for line in file3:
    print(line, end='') # 不自动加换行，打印原文
file3.close()
'''

'''
file4 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
line = file4.readline()
while len(line)!=0:
    print(line, end='')
    line = file4.readline()
file4.close()
'''

# 写文件
'''
file5 ='' open("E:\TDDOWNLOAD\helloworld.txt", "w")
file5.write("Hello Python")
file5.close()
'''

# 判断文件是否存在
"""
if os.path.exists("E:\TDDOWNLOAD\images\AggregatorIcon.gif"):
    print("文件存在")
else:
    print("文件不存在")

file1 = pathlib.Path("E:\TDDOWNLOAD\images\AggregatorIcon.gif")
if file1.exists():
    print("文件存在")
else:
    print("文件不存在")
"""

# 读二进制文件，以文本的方式读取，所以会自动 decode 为字符串
file1 = open("E:\\TDDOWNLOAD\\file1.dat", mode="rb")
#str1 = file1.read()
#print(str1)

#bytearr = str1.encode(encoding="gbk")
#print(bytearr.decode(encoding="utf-8"))  # abc

str1 = file1.read(4)
# 前三个字节都是0，对应字符是空
# 第四个字节是十进制110，正好对应小写字母n（110是文件中第一个字符的长度）
print(str1)  #    n

# python3中，以下三种写法都可以将 str 转为 byte数组
byte1 = str1.encode(encoding="utf-8")
print(byte1)  # b'\x00\x00\x00n'
print(type(byte1))  # <class 'bytes'>
'''
byte1 = bytes(str1, encoding="utf-8")
print(byte1)  # b'\x00\x00\x00n'
print(type(byte1))  # <class 'bytes'>
'''
'''
byte1 = bytearray(str1, encoding="utf-8")
print(byte1)  #bytearray(b'\x00\x00\x00n')
print(type(byte1))  # <class 'bytearray'>
'''
len1 = bytestoint(byte1)
print(len1)  # 110
str2 = file1.read(len1)
print(str2)

print("======================== 1 ==========================")

str3 = file1.read(4)
print(len(str3))  # 4
len1 = bytestoint(str3.encode(encoding="utf-8"))
print(len1)

str4 = file1.read(len1)
print(str4)  # 你好

str5 = file1.read(4)
print(len(str5))  # 0
