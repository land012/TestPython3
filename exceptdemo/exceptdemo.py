
import traceback
import unittest
import logging
import sys

__author__ = 'xudazhou'


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

def fn1():
    i1 = int("abc")


class ExceptionDemo(unittest.TestCase):

    """
    e=invalid literal for int() with base 10: 'abc'
    """
    @staticmethod
    def test1():
        try:
            i1 = int("abc")
        except Exception as e:
            logging.info("e=%s", e)

    """
    Traceback (most recent call last):
      File "D:\_python\TestPython3\exceptdemo\exceptdemo.py", line 33, in test2
        fn1()
      File "D:\_python\TestPython3\exceptdemo\exceptdemo.py", line 9, in fn1

        i1 = int("abc")
    ValueError: invalid literal for int() with base 10: 'abc'
    """
    @staticmethod
    def test2():
        try:
            fn1()
        except Exception as e:
            traceback.print_exc()

    @staticmethod
    def test3():
        try:
            fn1()
        except Exception as e:
            t, v, tb = sys.exc_info()
            print("type=%s" % t)  # type=<class 'ValueError'>

            print("type of value = %s" % type(v))  # type of value = <class 'ValueError'>
            print(v)  # invalid literal for int() with base 10: 'abc'
            print(str(v))  # invalid literal for int() with base 10: 'abc'
            print(v.args)  # ("invalid literal for int() with base 10: 'abc'",)

            # filename, lineno, functionname, msg = traceback.extract_tb(tb)
            # print("fin=%s, lineno=%d, fn=%s, msg=%s" % (filename, lineno, functionname, msg))
            tuple1 = traceback.extract_tb(tb)

            # tb=[<FrameSummary file D:\_python\TestPython3\exceptdemo\exceptdemo.py, line 49 in test3>, <FrameSummary file D:\_python\TestPython3\exceptdemo\exceptdemo.py, line 15 in fn1>]
            print("tb=%s" % tuple1)
            print(tuple1[0].filename)
