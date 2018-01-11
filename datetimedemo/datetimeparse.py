# coding: utf-8

import unittest
import datetime


class DateTimeParseFormat(unittest.TestCase):

    @staticmethod
    def test_parse1():
        """
        日期解析
        当 字符串长度和 pattern长度 不匹配时，会报错
        """
        dt1_str = "2017-01-08 15:03:45"  # 周日
        dt1 = datetime.datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S")
        print(dt1)
        print(dt1.weekday())  # 6

    @staticmethod
    def test_format1():
        """
        格式化时
        pattern 长度 可以小于 实际 date
        :return:
        """
        base_date = datetime.datetime.strptime("2017-09-14 00:00:00", "%Y-%m-%d %H:%M:%S")
        for i in range(5):
            l_str = "%s %s" % ("now", base_date.strftime("%Y%m%d"))
            print(l_str)
            base_date += datetime.timedelta(days=-1)
