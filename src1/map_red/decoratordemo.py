# coding: utf-8
import functools

__author__ = 'xudazhou'

def log(func):
    @functools.wraps(func)
    def wrapper(*args2, **kwargs):
        print("i am %s" % func.__name__)
        return func(*args2, **kwargs)

    return wrapper

@log
def now1():
    print("2017-07-14")

def now2():
    print("2017-07-14")

"""
i am now1
2017-07-14
"""
now1()
print("==================================")
"""
i am now2
2017-07-14
"""
log(now2)()
