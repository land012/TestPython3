#!/usr/bin/env python
# coding: utf-8

import unittest

__author__ = 'xudazhou'

class DictDemo(unittest.TestCase):
    @staticmethod
    def test1():
        """引用字典"""
        l_dict1 = {"k1": "v1", "k2": "v2"}
        print("dict1['k1']:%s" % l_dict1['k1'])  # 索引获取记录

    @staticmethod
    def test2():
        dict1 = {"k1": "v1", "k2": "v2"}
        dict1['k3'] = 'v3'  # 添加
        del dict1['k2']  # 删除
        print("dict1 count:%d" % len(dict1))  # 大小
        for k, v in dict1.items():  # 遍历
            print("dict1[%s]=%s" % (k, v), end=",")

    @staticmethod
    def test_exist():
        """判断 key 是否在字典中"""
        # 二维字典
        dict1 = { "k1" : { "k11" : "v11", "k12" : "v12" }, "k2" : { "k21" : "v21", "k22" : "v22" } }
        dict2 = {"k2": [4, 5, 6], "k3": [2, 3, 5], "k1": [1, 2, 3]}

        if 'k3' in dict1:  # 判断
            print('dict1[k3]:%s' % dict1['k3'])

        print(dict2["k2"][0])  # 4
        print(dict2.items())  # dict_items([('k2', [4, 5, 6]), ('k1', [1, 2, 3])])

    @staticmethod
    def test_exist2():
        """引用一个不存在的key，会报错"""
        dict2 = {"k2": [4, 5, 6], "k3": [2, 3, 5], "k1": [1, 2, 3]}
        # 报错 KeyError: 'k4'
        print(dict2["k4"])

    @staticmethod
    def test883():
        l_dict1 = {"k1": 1, "k2": 2}
        v1 = { k: v*2 for k, v in l_dict1.items() }
        print(v1)  # {'k2': 4, 'k1': 2}

        l1 = [ v for k, v in l_dict1.items()]
        print(l1)  # [1, 2]

    @staticmethod
    def test_sort1():
        dict2 = {"k2": [4, 5, 6], "k3": [2, 3, 5], "k1": [1, 2, 3]}
        print("k4" in dict2)  # False
        print(dict2)  # {'k3': [2, 3, 5], 'k2': [4, 5, 6], 'k1': [1, 2, 3]} # key的顺序每次执行是随机的
        keys = dict2.keys()  # 这个 keys 不是 list，不能直接调用 sort()
        print(keys)  # dict_keys(['k3', 'k2', 'k1'])

        keys = sorted(dict2.keys())
        print(dict2)  # {'k3': [2, 3, 5], 'k2': [4, 5, 6], 'k1': [1, 2, 3]} 原字典的顺序不变
        print(keys)  # ['k1', 'k2', 'k3']

    @staticmethod
    def test_sort2():
        """字典按 key 排序"""
        dict1 = {"k2": "v2", "k3": "v3", "k1": "v1"}
        list1 = sorted(dict1.items(), key=lambda item:item[0])
        for i in list1:
            print(i)

    @staticmethod
    def test_three():
        dict1 = { "k1": "v1" }
        print(dict1["k1"] if "k1" in dict1 else "null")



# ######################### 字典 ##########################


def test2342():
    l_dict1 = {"k1": "v1", "k2": "v2"}
    print(type(l_dict1.items()))  # <class 'dict_items'>


if __name__ == "__main__":
    test2342()
