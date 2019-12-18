# coding: utf-8
"""
# Created by xudazhou at 2019/9/18
"""
import unittest
import logging


class LoggingDemo(unittest.TestCase):

    @staticmethod
    def test1():
        # FileNotFoundError: [Errno 2] No such file or directory: 'D:\\_python\\TestPython3\\demo\\logs\\stdout.log'
        # 由于没有 logs 目录，所以报错
        logging.basicConfig(filename="logs/stdout.log",
                            level=logging.INFO,
                            format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info("hello logging")
