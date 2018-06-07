#!/usr/bin/python
# Filename : modulesecond.py


def say_hello():
    print("__name__=", __name__) # 当被其它模块引用时，打印 __name__= modulesecond
    if __name__ == "__main__":
        print("I am main")
    else:
        print("I am not main")
    print("Hello World")















