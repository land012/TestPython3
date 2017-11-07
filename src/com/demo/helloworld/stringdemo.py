__author__ = 'xudazhou'

# 格式化
# g
'''
print("%g" % 0.000454)    # 0.000454
print("%g" % 0.0000454)   # 4.54e-05
print("%g" % 0.00000454)  # 4.54e-06
'''

# dict
#print("%(a)s %(b)s" % {"a": "小王", "b": "小李"})  # 小王 小李


# split
# 默认以空白分隔
'''
str1 = "a  b c   d  e"
tuple1 = str1.split()
print(tuple1)  # ['a', 'b', 'c', 'd', 'e']
'''

# 字符串替换
str1 = "http://www.eaipatterns.com/img/ChannelIcon.gif"
# print(str1.replace("eaipatterns", "enterpriseintegrationpatterns"))


# str2_1 = "abc"
# str2_2 = "你好"
# str2_3 = ""
# print(len(str2_1))  # 3
# print(len(str2_2))  # 2
# print(len(str2_3))  # 0

'''
str1 = "aa"
str2 = "bb"
print(str1==str2)  # False
'''

'''
str3 = "a b c"
arr3 = str3.split()
print(arr3[0])  # a
print(len(arr3))  # 3
'''

# 按 \t 分割字符串
"""
str3_2 = "a	b	c"
arr3_2 = str3_2.split("\t")
print(type(arr3_2))  # <class 'list'>
print(len(arr3_2))  # 3
print(str3_2)  # a	b	c
print(arr3_2[1])  # b
"""

"""
str4 = "1.2 3"
arr4 = str4.split()
print(float(arr4[0]) + 0.5)
"""

def test89():
    # 首字母大写
    str1 = "asDceFs"
    print(str1.capitalize())  # Asdcefs


def test90():
    str2 = None
    print(str2 == "")  # False


def test91():
    str1 = "abcdefg"
    print(str1[:3])  # abc
    print(str1[-3:])  # efg


if __name__ == "__main__":
    test91()
