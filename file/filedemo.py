# coding: utf-8
"""
# Created by xudazhou at 2019/5/24
"""
import pathlib


if __name__ == "__main__":
    p = pathlib.Path("E:\TDDOWNLOAD\新建文件夹 (4)")

    for file1 in p.iterdir():
        file1_p = pathlib.Path(file1)
        for file2 in file1_p.iterdir():
            print(file2.name)
