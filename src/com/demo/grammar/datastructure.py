#!/usr/bin/python
__author__ = '大洲'

# ######################### 序列 ##########################

# 切片操作符 序号从0开始
# 取字符串子串也是这个语法
mylist = ["a", "b", "c", "d", "e"]
print("mylist[1:3]=%s" % mylist[1:3])  # 不包括索引为 3 的记录
print("mylist[:3]=%s" % mylist[:3])  # 从第一个开始
print("mylist[1:]=%s" % mylist[1:])  # 到最后一个
print("mylist[1:-1]=%s" % mylist[1:-1])  # 从索引为1的位置，到倒数第2个

'''
# 参考
# list1 = ["a", "b", "c"]
# list2 = list1
# del list1[0]
# print(list1)
# print(list2)
# 列表拷贝
# list3 = ["a", "b", "c"]
# list4 = list3[:]
# del list3[0]
# print(list3)
# print(list4)

# 字符串函数
name = "Hello"
print(name.startswith('Hel')) # True
print('e' in name)            # True
print(name.find("llo"))       # 2
print(name.find("world"))    # -1

delimiter = "#"
list1 = ["a", "b", "c"]
print(delimiter.join(list1)) # a#b#c
'''

str1 = "abcdef"
print(str1[1:-1])  # bcde

str2 = "name = %s" % str1
print(str2)  # name = abcdef
