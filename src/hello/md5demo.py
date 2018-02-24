# coding: utf-8

import unittest
import hashlib


class Md5Demo(unittest.TestCase):

    @staticmethod
    def test1():
        str1 = "abc"
        md5a = hashlib.md5()
        md5a.update(str1.encode(encoding='utf-8'))
        print(md5a.digest())
        print(md5a.hexdigest())

        f1 = open("E:\\TDDOWNLOAD\\_temp\\helloworld.txt", mode="w", encoding="utf-8")
        f1.write(str1)
        f1.close()

    @staticmethod
    def test2():
        f1 = open(".")


