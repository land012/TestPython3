__author__ = 'xudazhou'

import pathlib
import os
import mimetypes
import unittest

'''
处理指定路径下的所有文本文件
'''

class PathlibDemo(unittest.TestCase):

    @staticmethod
    def test1():
        p = pathlib.Path("F:\\ccc\\txt")

        # mimetypes.add_type("text/plain", "txt")

        for file in p.iterdir():
            # print(file)  # F:\ccc\txt\1.jpg
            fname = file.name
            # print(fname)  # 1.jpg

            if file.is_file():
                ext = os.path.splitext(fname)
                # print(ext)  # ('1', '.jpg')
                # print(mimetypes.types_map[ext[1]])  # text/plain
                if ext[1] == ".txt":
                    print(file)

    @staticmethod
    def test2():
        """
        只能删除空文件夹
        :return:
        """
        p = pathlib.Path("E:\\TDDOWNLOAD\\temp1")
        p.rmdir()

    @staticmethod
    def test3():
        """
        获取文件顺序
        1.txt
        10.txt
        11.txt
        2.txt
        3.txt
        :return:
        """
        p = pathlib.Path("E:\TDDOWNLOAD\新建文件夹 (3)")

        for file in p.iterdir():
            # print(file)  # F:\ccc\txt\1.jpg
            fname = file.name
            print(fname)  # 1.jpg

    @staticmethod
    def test4():
        """
        只返回子文件名，不包含路径
        :return:
        """
        list1 = os.listdir("E:\TDDOWNLOAD")
        print(list1)
