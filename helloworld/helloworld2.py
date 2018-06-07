#!/usr/bin/python
# Filename : helloworld.py

import unittest

class HelloWorld(unittest.TestCase):

    @staticmethod
    def test_None():
        l1 = None
        if l1 is None:
            print("i am None")
        else:
            print("i am not None")

    @staticmethod
    def test_chinese():
        """可以直接使用中文，不需要指定 coding"""
        print("这里是中文")

    @staticmethod
    def test_multiline():
        # 多行字符串
        print("""Hello
        World""")

    @staticmethod
    def test_singleline():
        # 单行字符串
        print("Hello \
World")

# 不会进行转义
#print(r"newline is indicated by \n")

'''
# print 参数
print("a", "b", "c") # 默认以空格分隔
print("a", "b", "c", sep="|") # 指定关键参数sep为“|”，以“|”分隔

t1 = "a"
t2 = "b"
print(t1, t2)
'''

# 双引号
'''
t1 = "a"
print("haha=" + t1)  # haha=a
'''



