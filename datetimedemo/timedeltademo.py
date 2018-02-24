__author__ = 'xudazhou'

import datetime
import unittest


class TimeDeltaDemo(unittest.TestCase):

    @staticmethod
    def test1():
        dt1 = datetime.datetime.today()
        print(dt1)

        dt2 = dt1 + datetime.timedelta(days = -1)
        print(dt2)
        print(dt2.strftime("%Y-%m-%d %H:00:00"))  # 2016-12-15 10:00:00


    @staticmethod
    def test2():
        date1 = datetime.datetime.strptime("2018-01-09", "%Y-%m-%d")
        date2 = date1 + datetime.timedelta(days=-90)
        print(date2)
