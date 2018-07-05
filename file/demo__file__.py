# coding: utf-8
import os


if __name__ == "__main__":
    # 当前文件名
    print(__file__)  # D:/_python/TestPython3/src/com/demo/helloworld/helloworld.py
    cur_filename = __file__.split(os.sep)[-1]
    print(cur_filename)  # helloworld.py
