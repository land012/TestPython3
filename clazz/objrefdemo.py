# coding: utf-8

"""
值引用 和 对象引用
"""
import unittest
import datetime
import person


class ObjrefTest(unittest.TestCase):

    @staticmethod
    def test1():
        """值引用"""
        dt1 = datetime.datetime.strptime("2017-12-12", "%Y-%m-%d")
        dt2 = dt1
        dt1 += datetime.timedelta(days=-2)
        print(dt1)  # 2017-12-10 00:00:00
        print(dt2)  # 2017-12-12 00:00:00

    @staticmethod
    def test2():
        """对象引用"""
        p1 = person.Person("tom")
        p2 = p1
        p1.name = "jim"
        p1.sayhello()  # Hello jim
        p2.sayhello()  # Hello jim
