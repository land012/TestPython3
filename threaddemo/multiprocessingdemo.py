# coding:utf-8
from multiprocessing import Process
import multiprocessing
import os
import time

__author__ = 'xudazhou'
"""
子进程
"""


def run_proc(name, p_flag):
    while p_flag.is_set():
        time.sleep(1)
        print("i am child %s, pid is %s" % (name, os.getpid()))


if __name__ == "__main__":
    print("i am parent process %s" % os.getpid())
    flag = multiprocessing.Event()
    flag.set()
    p = Process(target=run_proc, args=("child1", flag))
    p.start()
    print("i am parent process %s, 2" % os.getpid())
    time.sleep(3)
    flag.clear()
    print("end %d" % multiprocessing.cpu_count())  # end 2

