__author__ = 'xudazhou'


def test1():
    dict1 = { "k1" : "v1", "k2" : "v2" }

    """
    k 1
    k 2
    """
    for k, v in dict1:
        print(k, v)

    print("==================== 1 =====================")

    """
    默认打印 key
    k1
    k2
    """
    for k in dict1:
        print(k)


def test2():
    dict1 = {"k1": "v1"}
    print(dict1.get("k1"))  # v1
    print(dict1["k1"])  # v1



if __name__ == "__main__":
    test2()
