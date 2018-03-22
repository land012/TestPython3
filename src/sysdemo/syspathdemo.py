# coding: utf-8

import unittest
import sys

sys.path.append("D:\\_python\\TestPython3\\helloworld")

import helloworld

class Syspathdemo(unittest.TestCase):

    @staticmethod
    def test1():
        helloworld.hello("Tom")
