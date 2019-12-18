# coding: utf-8
"""
# Created by xudazhou at 2019/5/15
"""

import unittest
import shutil

class ShutilDemo(unittest.TestCase):

    @staticmethod
    def test1():
        shutil.rmtree("E:\\TDDOWNLOAD\\temp1", ignore_errors=True)
