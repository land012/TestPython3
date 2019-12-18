# coding:utf-8
import time
import threading
import subprocess

__author__ = 'xudazhou'

k1 = "v1"


def run_thread(p_sec):
    # 全局变量 k1 可以传进来
    time.sleep(p_sec)
    subprocess.call("echo %cd%", shell=True)
    print("thread %s is running %s" % (threading.current_thread().name, k1))


if __name__ == "__main__":
    print("thread %s is begin" % threading.current_thread().name)
    t = threading.Thread(target=run_thread, name="child_thread", args=(3,))
    t.start()
    t2 = threading.Thread(target=run_thread, name="child_thread2", args=(2,))
    t2.start()
    # t.join()
    print("thread %s is end" % threading.current_thread().name)
