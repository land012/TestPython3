# coding: utf-8

import unittest
from memory_profiler import profile

@profile
def fn1():
    list1 = list()
    for i in range(20000):
        list1.append(str(i))
    print(len(list1))


class MemoryProfilerDemo(unittest.TestCase):

    @staticmethod
    def test1():
        fn1()
