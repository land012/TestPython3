# coding: utf-8


def test1():
    set1 = set([1, 2, 2, 3])
    set1.add(7)
    print(set1)


if __name__ == "__main__":
    test1()  # {1, 2, 3, 7}
