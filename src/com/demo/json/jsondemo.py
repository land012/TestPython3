# coding:utf-8
import urllib
import json

__author__ = 'xudazhou'

# 手动 raise 异常
"""
if True:
    raise RuntimeError("error")
"""

dict1 = {"k1": "v1", "k2": "v2"}
dict2 = {"d1": dict1}
jsonstr = json.dumps(dict2)
print(jsonstr)  # {"d1": {"k2": "v2", "k1": "v1"}}

