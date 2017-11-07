# coding:utf-8
from multiprocessing import Process
import multiprocessing
import os

__author__ = 'xudazhou'
"""
子进程
"""


def run_proc(name):
    print("i am child %s, pid is %s" % (name, os.getpid()))


if __name__ == "__main__":
    print("i am parent process %s" % os.getpid())
    p = Process(target=run_proc, args=("child1", ))
    p.start()
    print("i am parent process %s, 2" % os.getpid())
    p.join()
    print("end %d" % multiprocessing.cpu_count())  # end 2

