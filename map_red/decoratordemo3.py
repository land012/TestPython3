# coding: utf-8
import functools
import logging

__author__ = 'xudazhou'

logg = logging.getLogger("log")
logg.setLevel(logging.DEBUG)
loghandler = logging.StreamHandler()
logg.addHandler(loghandler)

def log(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **kwargs):
            logg.info("decorator args num = %d" % len(args1))
            return func(*args2, **kwargs)

        return wrapper

    if len(args1) > 0:
        # @log 这种用法
        if hasattr(args1[0], "__call__"):
            logg.info("====================if 1")
            return decorator(args1[0])
        else:
            logg.info("====================if 2")
            return decorator
    else:
        logg.info("====================if 3")
        return decorator

@log
def now2():
    logg.info("i am now2")

@log()
def now3():
    logg.info("i am now3")

logg.info("=========================== begin ===================================")

"""
decorator args num = 1
i am now2
"""
now2()
logg.info("==================== 1 ========================")
now3()
