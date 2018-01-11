# coding: utf-8

import unittest
import objgraph
import logging
import sys


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def fun1():
    objgraph.show_growth(limit=5, file=sys.stderr)
    logging.info("=========================================")

    l1 = list()
    for i in range(7000):
        l1.append(i)

    objgraph.show_growth(limit=5, file=sys.stderr)
    logging.info("=========================================")

    dict1 = dict()
    for i in range(2000):
        u = User(i, str(i))
        dict1[i] = u

    objgraph.show_growth(limit=5, file=sys.stderr)
    logging.info("=========================================")


class User(object):
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name


class ObjgraphDemo(unittest.TestCase):

    @staticmethod
    def test1():
        fun1()


# if __name__ == "__main__":
#     fun1()
