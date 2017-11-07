# coding:utf-8
from multiprocessing import Pool
import os
import time

__author__ = 'xudazhou'

def task(name):
    print("i am child %s %s, parent is %s begin" % (name, os.getpid(), os.getppid()))
    time.sleep(3)
    print("i am child %s %s, parent is %s end" % (name, os.getpid(), os.getppid()))


if __name__ == "__main__":
    print("i am main process %s" % os.getpid())
    pool = Pool(3)

    for i in range(4):
        pool.apply_async(func=task, args=(i, ))

    pool.close()
    pool.join()
    print("end")