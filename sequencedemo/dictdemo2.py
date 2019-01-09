__author__ = 'xudazhou'

import unittest

class Dictdemo2(unittest.TestCase):

    @staticmethod
    def test1():
        dict1 = { "ka" : "v1", "kb" : "v2" }

        """
        只打印了key，且如果key 有三个字符，则会报错
        k a
        k b
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


    def test2(self):
        dict1 = {"k1": "v1"}
        print(dict1.get("k1"))  # v1
        print(dict1["k1"])  # v1

    @staticmethod
    def test3():
        dict1 = dict()
        dict1["k1"] = "v1"
        dict1.setdefault("k1", "v11")
        dict1.setdefault("k2", "v22")
        print(dict1)

    @staticmethod
    def test_dictinit():
        dict1 = dict({"k1": "v1"})
        print(dict1)

        # 报错
        # dict2 = dict("k2"="v2")
        # print(dict2)

        # ???
        dict3 = dict(("k3", "v3"))
        print(dict3)  # {'v': '3', 'k': '3'}
