# coding: utf-8
import os
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # 当前文件名
    logging.info(__file__)  # D:/_python/TestPython3/src/com/demo/helloworld/helloworld.py 实际上是执行命令的第一个参数 sys.argv[0]
    logging.info(os.sep)  # \
    cur_filename = __file__.split(os.sep)[-1]
    logging.info(cur_filename)  # helloworld.py
    logging.info(os.getcwd())  # D:\_python\TestPython3\file
    logging.info(os.path.abspath(__file__))  # D:\_python\TestPython3\file\demo__file__.py
    logging.info(os.curdir)  # .
