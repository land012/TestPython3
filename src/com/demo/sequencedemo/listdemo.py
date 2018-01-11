# coding: utf-8

__author__ = 'xudazhou'

"""
下标从 0 开始
"""
import unittest
import operator


class ListDemo(unittest.TestCase):

    @staticmethod
    def test_append():
        l_shoplist = ["apple", "mango", "carrot", "radish"]
        print("shoplist:", l_shoplist)
        l_shoplist.append("banana")  # 追加记录

    @staticmethod
    def test_del():
        l_shoplist = ["apple", "mango", "carrot", "radish", "banana"]
        olditem = l_shoplist[0]
        del l_shoplist[0]  # 删除列表记录
        print("olditem:", olditem)
        print("shoplist:", l_shoplist)

    @staticmethod
    def test_sort():
        l_shoplist = ["apple", "mango", "carrot", "radish", "banana" ]
        l_shoplist.sort() # 列表排序
        print("sorted shoplist:", l_shoplist)
        print("shoplist[0]:", l_shoplist[0]) # 获取指定索引记录

    @staticmethod
    def test_repli():
        # 可以有重复记录
        mylist = [ "history", "english", "history" ]
        print(mylist)
        print(len(mylist))
        mylist.sort()
        print(mylist)

    @staticmethod
    def test123():
        # 判断是否包含
        list6 = ["a", "b", "c", "de"]
        print("a" in list6)  # True
        print("d" in list6)  # False
        print(list6.reverse())  # None

        # list6 已经变为逆序
        """
        for e in list6:
            print(e)
        """

        """
        0 - de
        1 - c
        2 - b
        3 - a
        """
        for i, v in enumerate(list6):
            print("%d - %s" % (i, v))

    @staticmethod
    def test_sort_obj():
        """使用 lambda"""
        list1 = list()
        u1 = User(1, "tom")
        u2 = User(2, "jim")
        u3 = User(3, "lucy")
        list1.append(u1)
        list1.append(u2)
        list1.append(u3)
        print(u1)  # 走 __str__()
        print(list1)  # 走 __repr__() [User[1, tom], User[2, jim], User[3, lucy]]

        list1.sort(key=lambda i:i.name)
        print(list1)  # [User[2, jim], User[3, lucy], User[1, tom]]

    @staticmethod
    def test_sort_obj2():
        """使用 operater.attrgetter"""
        list1 = list()
        u1 = User(1, "tom")
        u2 = User(2, "jim")
        u3 = User(3, "lucy")
        list1.append(u1)
        list1.append(u2)
        list1.append(u3)
        print(list1)  # 走 __repr__() [User[1, tom], User[2, jim], User[3, lucy]]

        f = operator.attrgetter("name")

        list1.sort(key=f)
        print(list1)  # [User[2, jim], User[3, lucy], User[1, tom]]

    @staticmethod
    def test_sort_dict():
        """对 dict 排序"""
        dict1 = {"k1": 3, "k2": "v2"}
        dict2 = {"k1": 2, "k2": "v1"}
        dict3 = {"k1": 4, "k2": "v3"}
        list1 = [dict1, dict2, dict3]
        print(list1)  # [{'k2': 'v2', 'k1': 3}, {'k2': 'v1', 'k1': 2}, {'k2': 'v3', 'k1': 4}]
        list1.sort(key=lambda d: d["k1"])
        print(list1)  # [{'k2': 'v1', 'k1': 2}, {'k2': 'v2', 'k1': 3}, {'k2': 'v3', 'k1': 4}]
        print(max(list1, key=lambda d: d["k1"]))  # {'k1': 4, 'k2': 'v3'}


class User(object):

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def __str__(self):
        return "User[%s, %s]" % (self.uid, self.name)

    def __repr__(self):
        return self.__str__()

# ######################### 列表 ##########################
#shoplist = [ "apple", "mango", "carrot", "radish" ]
#print("items count:", len(shoplist)) # 列表大小
#print(shoplist)

#print("===============================")

# 遍历
#for i in shoplist:
#    print(i, end=" ")

#print()
#print("===============================")



# 列表中有字典
'''
mylist3 = []
for i in range(1, 4):
    mylist3.append({ "i" : i })

print(mylist3) # [{'i': 1}, {'i': 2}, {'i': 3}]
'''

# 空列表 不会报错
'''
list4 = []
for i in list4:
    print(i)
'''

# 下标越界的报错
# list5 = [1, 2]
# 报错 下标越界
# IndexError: list assignment index out of range
#list5[2] = 3

# IndexError: list index out of range
# print(list5[2])



