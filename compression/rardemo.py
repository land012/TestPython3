# coding: utf-8
"""
# Created by xudazhou at 2019/8/27
"""
import unittest
import rarfile


rarfile.UNRAR_TOOL = r"D:\Program Files\WinRAR\UnRAR.exe"


class RarDemo(unittest.TestCase):

    @staticmethod
    def test1():
        rfile = rarfile.RarFile(r"E:\TDDOWNLOAD\down_game.rar")

        # rfile.setpassword("123456")

        for e in rfile.namelist():
            print(e)

        # 不指定密码则报错
        # rarfile.RarCRCError: CRC error during unpacking [3]
        rfile.extractall(path=r"E:\TDDOWNLOAD")
