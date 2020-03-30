# coding:utf-8

import urllib
import json
import unittest

__author__ = 'xudazhou'

# 手动 raise 异常
"""
if True:
    raise RuntimeError("error")
"""

class JsonDemo(unittest.TestCase):

    @staticmethod
    def test1():
        dict1 = {"k1": "v1", "k2": "v2"}
        dict2 = {"d1": dict1}
        jsonstr = json.dumps(dict2)
        print(jsonstr)  # {"d1": {"k2": "v2", "k1": "v1"}}

    @staticmethod
    def test2():
        list1 = list([1, 2, 3])
        dict1 = dict({"k1": list1, "k2" : "v2"})
        json_str = json.dumps(dict1)
        print(json_str)
        dict2 = json.loads(json_str)
        print(type(dict2))  # <class 'dict'>
        print(type(dict2["k1"]))  # <class 'list'>
        print(dict2)
