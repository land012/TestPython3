__author__ = 'xudazhou'

def fn1():
    if True:
        raise Exception


if __name__ == "__main__":
    try:
        fn1()
    except Exception:
        print("exception")