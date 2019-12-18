# coding: utf-8

import os
import unittest


class HelloTest(unittest.TestCase):

    @staticmethod
    def test_hello():
        print("Hello %s" % "tom")

        print("a" + "b" if 1 == 1 else "c")  # ab
        print("a" + "b" if 1==2 else "c")  # c

    @staticmethod
    def test_main():
        print(os.getcwd())  # D:\_python\TestPython3\helloworld
        print(__file__)  # D:/_python/TestPython3/helloworld/helloworld.py
