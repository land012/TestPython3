
import traceback


__author__ = 'xudazhou'

def fn1():
    if True:
        raise Exception


if __name__ == "__main__":
    try:
        fn1()
    except Exception as e:
        traceback.print_exc()
        print(e)
        print("exception")