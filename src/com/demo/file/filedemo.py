import os
import pathlib

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


file4 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
line = file4.readline()
while len(line)!=0:
    print(line, end='')
    line = file4.readline()
file4.close()


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


