__author__ = 'xudazhou'

import sys


if __name__ == "__main__":
    print("====================== 1 ===========================")
    # ['D:/_python/TestProj/src/com/demo/module/sysdemo.py', 'haha', 'heihei']
    print(len(sys.argv))  # 3
    print(sys.argv)
    print(sys.argv[0])  # 0 是脚本本身 D:/_python/TestPython3/src/com/demo/sysdemo/sysargvdemo.py
    print(sys.argv[1])  # haha
    print("====================== 2 ===========================")


    # 命令行参数
    '''
    D:\ProgramDev\Python34\python.exe D:/_python/TestProj/src/com/demo/module/sysdemo.py haha -k1=v1
    输出:
    D:/_python/TestProj/src/com/demo/module/sysdemo.py
    haha
    -k1=v1
    '''

    for i in sys.argv:
        print(i)
