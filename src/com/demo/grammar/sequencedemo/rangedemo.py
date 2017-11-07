__author__ = 'xudazhou'

def test1():
    for i in range(3, 5):
        print(i, end=" ")  # 3 4


def test2():
    # 指定步长
    for i in range(1, 10, 2):
        print(i, end=" ")  # 1 3 5 7 9


def test3():
    for i in range(0, 0):
        print(i, end=" ")  # 3 4


if __name__ == "__mainn__":
    test3()
