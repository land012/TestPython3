# coding:utf-8
import time
import threading

__author__ = 'xudazhou'

k1 = "v1"


def run_thread():
    # 全局变量 k1 可以传进来
    print("thread %s is running %s" % (threading.current_thread().name, k1))


if __name__ == "__main__":
    print("thread %s is begin" % threading.current_thread().name)
    t = threading.Thread(target=run_thread, name="child_thread")
    t.start()
    t.join()
    print("thread %s is end" % threading.current_thread().name)
