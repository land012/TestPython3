# coding:utf-8
from functools import reduce

__author__ = 'xudazhou'

"""
字符串 转 float
"""

def chartonum(x):
    return int(x)

def integerpart(x, y):
    return x * 10 + y

def decimalpart(x, y):
    return x / 10 + y

def strtofloat(str1):
    list1 = str1.split(".")

    num1 = reduce(lambda x, y : x * 10 + y, map(chartonum, list1[0]))

    list2 = list(map(chartonum, list1[1]))
    list2.reverse()
    list2.append(0)
    num2 = reduce(decimalpart, list2)
    return num1 + num2

str1 = "123.456"
f1 = strtofloat(str1)
print(type(f1))  # <class 'float'>
print(f1)  # 123.456
