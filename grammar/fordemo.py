#!/usr/bin/python
# Filename: fordemo.py

import unittest

class ForDemo(unittest.TestCase):

    @staticmethod
    def test_fn1():
        """不会打印 5"""
        for i in range(2, 5):
            if i == 3:
                continue
            print(i)
        #    if i==3:
        #        break
        else:
            print("Loop is End!")

    @staticmethod
    def test_fn2():
        l1 = [ x * 2 for x in range(1, 3) ]
        print(l1)  # [2, 4]
