#!/usr/bin/python

import unittest


# 函数
def sayHello():
    print("Hello World")


# 带形参的函数
def say_hello2(name):
   print("Hello", name)


# 全局变量和局部变量
# 这中写法，x 在函数中被认为是全局变量
def fn1():
    print("x is", x)


# 这种写法是错误的，x 被认为是局部变量
# UnboundLocalError: local variable 'x' referenced before assignment
#def fn2():
#    print("x is", x)
#    x = 2

x = 20


# 默认参数值
def fn3(msg, times = 1):
    print(msg * times)
# 调用有默认参数的函数
#fn3("hello")
#fn3("Hello", 2)


def fn4(msg, times):
    print(msg * times)
# 这种调用方式会报错 TypeError: fn4() missing 1 required positional argument: 'times'
#fn4("tom")

# 这种定义会报错 SyntaxError: non-default argument follows default argument
# 非默认参数 不能 在默认参数后面
#def fn5(a=1, b, c=3):
#    print("a=", a, ",b=", b, ",c=", c)


# 关键参数
def fn6(a, b=11, c=21):
    print("a=", a, ", b=", b, ", c=", c)

#fn6(1, 12)
#fn6(2, c=22)


# 函数内定义函数
def fn7(y):
    def fn7_1(x):
        return x * 2;

    return fn7_1(y) + 1


def fn10():
    for i in range(1, 5):
        if i == 2:
            return i
    return 10


class FunctionDemo(unittest.TestCase):

    @staticmethod
    def test1():
        sayHello()

    @staticmethod
    def test2():
        say_hello2("Tom")

    @staticmethod
    def test3():
        """在函数中引用全局变量"""
        fn1()

    @staticmethod
    def test9():
        print(fn7(2))  # 5
        print(isinstance(fn7, str))  # False
        print(hasattr(fn7, "__call__"))  # True

    @staticmethod
    def test10():
        """在 for 循环中使用 return，方法直接返回"""
        print(fn10())  # 2
