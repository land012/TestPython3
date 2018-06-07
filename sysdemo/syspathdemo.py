# coding: utf-8

import unittest
import sys

sys.path.append("D:\\_python\\TestPython3\\helloworld\\helloworld.py")

import helloworld

"""
# 手工跑单测
# 引号中的双斜线要换成单斜线
python "D:\ProgramDev\PyCharm 2016.3.3\helpers\pycharm\\utrunner.py" D:\\_python\\TestPython3\\src\\sysdemo\\syspathdemo.py::Syspathdemo::test1 true
"""
class Syspathdemo(unittest.TestCase):

    @staticmethod
    def test1():
        helloworld.hello("Tom")
