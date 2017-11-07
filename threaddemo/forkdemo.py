# coding:utf-8
import os
__author__ = 'xudazhou'

print("process id %s" % os.getpid())
pid = os.fork()

# if 和 else 都会被执行
# 因为当前进程被复制了一份，父子进程都会走到下面的逻辑
if pid == 0:
    print("i am child %s, parent is %s" % (os.getpid(), os.getppid()))
else:
    print("i am %s, my child is %s" % (os.getpid(), pid))
