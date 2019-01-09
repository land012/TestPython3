__author__ = 'xudazhou'

import datetime
import unittest
import hectortimeutils


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

    @staticmethod
    def test3():
        date1 = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
        print(type(date1))  # <class 'datetime.datetime'>
        print(date1)  # 2016-06-15 00:00:00
        print(date1.weekday())  # 2
        print(date1.isoweekday())  # 3

    # 计算周数
    @staticmethod
    def test3_1():
        """
        计算周数
        周一 至 周一，是 1周
        :return:
        """
        date1 = datetime.datetime.strptime("2016-06-13", "%Y-%m-%d")  # mon
        date2 = datetime.datetime.strptime("2016-06-20", "%Y-%m-%d")
        date3 = datetime.datetime.strptime("2018-12-24", "%Y-%m-%d")
        print(hectortimeutils.cal_weeks(date1, date2))  # (25, 0)
        print(hectortimeutils.cal_weeks(date1, date3))  # (29, 0)

    @staticmethod
    def test4():
        date1 = datetime.datetime.strptime("2018-10-19", "%Y-%m-%d")
        date2 = datetime.datetime.strptime("2018-11-11", "%Y-%m-%d")
        timedelta1 = date2 - date1
        print(type(timedelta1))  # <class 'datetime.timedelta'>
        print(timedelta1)  # 6 days, 0:00:00y
        # AttributeError: 'datetime.timedelta' object has no attribute 'weeks'
        # print(timedelta1.weeks)
        print(timedelta1.days)  # 6
        print(timedelta1.seconds)  # 0

    @staticmethod
    def test5():
        date1 = datetime.datetime.strptime("2018-07-22", "%Y-%m-%d")
        date2 = datetime.datetime.strptime("2018-08-04", "%Y-%m-%d")
        while date1 <= date2:
            print(date1.strftime("%Y%m%d"))
            date1 = date1 + datetime.timedelta(days=1)




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TimeDeltaDemo('test1'))
    suite.addTest(TimeDeltaDemo('test3'))
    suite.addTest(TimeDeltaDemo('test3_1'))
    suite.addTest(TimeDeltaDemo('test4'))

    unittest.TextTestRunner(verbosity=2).run(suite)
