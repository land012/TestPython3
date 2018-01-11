# coding: utf-8

import unittest
import collections
import json

class OrderedDictDemo(unittest.TestCase):
    @staticmethod
    def test2():
        """将无序字典转为有序"""
        dict1 = dict()
        dict1["k1"] = "v1"
        dict1["k2"] = "v2"
        dict1["k3"] = "v3"
        print(dict1)  # {'k1': 'v1', 'k3': 'v3', 'k2': 'v2'}
        print(json.dumps(dict1))  # {"k1": "v1", "k2": "v2", "k3": "v3"}

        dict2 = collections.OrderedDict(sorted(dict1.items(), key=lambda i:i[0]))
        print(dict2)  # OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
        print(json.dumps(dict2))  # {"k1": "v1", "k2": "v2", "k3": "v3"}

    @staticmethod
    def test1():
        """字典 key 顺序是初始化的顺序"""
        dict1 = collections.OrderedDict()
        dict1["k2"] = "v2"
        dict1["k1"] = "v1"
        dict1["k3"] = "v3"
        print(dict1)  # OrderedDict([('k2', 'v2'), ('k1', 'v1'), ('k3', 'v3')])
        json_str = json.dumps(dict1)
        print(json_str)  # {"k2": "v2", "k1": "v1", "k3": "v3"}

        print(dict1["k2"])  # v2
        dict2 = json.loads(json_str)
        print(type(dict2))  # <class 'dict'>
        print(dict2)  # {'k3': 'v3', 'k1': 'v1', 'k2': 'v2'}
