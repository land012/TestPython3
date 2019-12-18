# coding: utf-8
"""
# Created by xudazhou at 2019/8/26
"""

import unittest
import zipfile


class ZipDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print(zipfile.is_zipfile(r"E:\TDDOWNLOAD\down_game.rar"))  # False
        print(zipfile.is_zipfile(r"E:\TDDOWNLOAD\down_game.zip"))  # True

    @staticmethod
    def test2():
        zfile = zipfile.ZipFile(r"E:\TDDOWNLOAD\down_game.zip")
        zfile.setpassword("123456".encode(encoding="utf-8"))
        # print(zfile.infolist())
        for e in zfile.namelist():
            print(e.encode(encoding="cp437").decode(encoding="gbk"))  # 中文文件名乱码

        zfile.extractall(path=r"E:\TDDOWNLOAD")  # 中文文件名乱码

    @staticmethod
    def test3():
        zfile = zipfile.ZipFile(r"E:\TDDOWNLOAD\down_game.zip")
        zfile.setpassword("12356".encode(encoding="utf-8"))

        # 这个函数不受密码影响
        for e in zfile.infolist():
            filepath = e.filename.split("/")
            print(e.filename)
            # print(filepath)

        # RuntimeError: Bad password for file
        zfile.extractall()
