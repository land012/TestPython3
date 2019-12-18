# coding: utf-8

import time
import datetime
import unittest


class DatetimeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        start = datetime.datetime.now()
        print(start)  # 2019-09-10 22:43:30.331978
        time.sleep(3)
        delta1 = datetime.datetime.now() - start
        print(delta1)  # 0:00:03.004172
        print(delta1.days)  # 0
        print(delta1.seconds)  # 3
        print(delta1.microseconds)  # 172

    @staticmethod
    def test_delta():
        start = datetime.datetime.strptime("2017-12-01 14:12:15", "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime("2017-12-01 14:13:20", "%Y-%m-%d %H:%M:%S")
        delta1 = end - start
        print(delta1)  # 0:01:05
        print(delta1.days)  # 0
        print(delta1.seconds)  # 65
        print(delta1.microseconds)  # 0
        print(delta1.total_seconds())  # 65

    @staticmethod
    def test_delta2():
        start = datetime.datetime.strptime("2017-12-01 14:12:15", "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime("2017-12-02 14:12:20", "%Y-%m-%d %H:%M:%S")
        delta1 = end - start
        print(delta1)  # 1 day, 0:00:05
        print(delta1.days)  # 1
        print(delta1.seconds)  # 5
        print(delta1.microseconds)  # 0
        print(delta1.total_seconds())  # 86405.0

    @staticmethod
    def test_dateparse():
        date1 = datetime.datetime.strptime("2017-12-12 00:00:00"[:10], "%Y-%m-%d")
        print(date1)

    @staticmethod
    def test5():
        print(datetime) # <module 'datetime' from 'D:\\ProgramDev\\Python34\\lib\\datetime.py'>
        print(datetime.date) # <class 'datetime.date'>
        print(datetime.time) # <class 'datetime.time'>
        print(datetime.datetime) # <class 'datetime.datetime'>

    @staticmethod
    def test6():
        # datetime.date
        today = datetime.date.today()
        print(today)  # 2017-01-22
        print(today.day)  # 22
        print(today.weekday())  # 6 周日
        print(today.strftime("%Y-%m-%d")) # 2016-07-21






'''
print(datetime.datetime.today().hour)  # 11
'''

"""
print(datetime.datetime.today().date())
# print(datetime.datetime.date())

dt1 = datetime.datetime(2017,3,29,12,00,1)
print(dt1)
"""

'''
# 时间戳转化为日期
# 2016-08-29 15:13:14
timestamp1 = 1472454794
# 2016-08-29 07:13:14
print(datetime.datetime.utcfromtimestamp(timestamp1))
# 2016-08-29 15:13:14
print(datetime.datetime.fromtimestamp(timestamp1))
'''



# 1492790400
# 1492790400
# 1492790400
"""
print(datetime.datetime.fromtimestamp(1492790400))  # 2017-04-22 00:00:00
"""
