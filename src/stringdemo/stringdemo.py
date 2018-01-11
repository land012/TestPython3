# coding: utf-8

import unittest

__author__ = 'xudazhou'


class StringDemo(unittest.TestCase):

    @staticmethod
    def test3():
        """
        split
        默认以空白分隔
        返回 list
        :return:
        """
        l_str1 = "a  b c   d  e"
        tuple1 = l_str1.split()
        print(type(tuple1))  # <class 'list'>
        print(tuple1)  # ['a', 'b', 'c', 'd', 'e']
        del tuple1[2]
        print(tuple1)  # ['a', 'b', 'd', 'e']

    @staticmethod
    def test_replace():
        # 字符串替换
        str1 = "http://www.eaipatterns.com/img/ChannelIcon.gif"
        # print(str1.replace("eaipatterns", "enterpriseintegrationpatterns"))
        print("a b".replace(" ", "\ "))

    @staticmethod
    def test_len():
        str2_1 = "abc"
        str2_2 = "你好"
        str2_3 = ""
        print(len(str2_1))  # 3
        print(len(str2_2))  # 2
        print(len(str2_3))  # 0

    @staticmethod
    def test_strbool():
        str1 = "aa"
        str2 = "bb"
        print(str1==str2)  # False

    @staticmethod
    def test_split():
        str3 = "a b c"
        arr3 = str3.split()
        print(arr3[0])  # a
        print(len(arr3))  # 3

    @staticmethod
    def test_split2():
        # 按 \t 分割字符串
        str3_2 = "a	b	c"
        arr3_2 = str3_2.split("\t")
        print(type(arr3_2))  # <class 'list'>
        print(len(arr3_2))  # 3
        print(str3_2)  # a	b	c
        print(arr3_2[1])  # b

    @staticmethod
    def test_split3():
        str4 = "1.2 3"
        arr4 = str4.split()
        print(float(arr4[0]) + 0.5)

    @staticmethod
    def test89():
        # 首字母大写
        str1 = "asDceFs"
        print(str1.capitalize())  # Asdcefs

    @staticmethod
    def test90():
        str2 = None
        print(str2 == "")  # False

    @staticmethod
    def test91():
        str1 = "abcdefg"
        print(str1[:3])  # abc
        print(str1[-3:])  # efg



    @staticmethod
    def test_isalnum():
        print("a".isalnum())  # True
        print("1".isalnum())  # True
        print("a1".isalnum())  # True
        print("a1_".isalnum())  # False
        print("_".isalnum())  # False

    @staticmethod
    def test_isalpha():
        print("a".isalpha())  # True
        print("A".isalpha())  # True
        print("1".isalpha())  # False
        print("a1".isalpha())  # False

    @staticmethod
    def test_isdecimal():
        print("a".isdecimal())  # False
        print("1".isdecimal())  # True
        print("1.1".isdecimal())  # False
        print("-1".isdecimal())  # False
        print("01".isdecimal())  # True
        print("Ⅶ".isdecimal())  # False
        print("一".isdecimal())  # False
        print("\u00b3".isdecimal())  # False

    @staticmethod
    def test_isdigit():
        print("a".isdigit())  # False
        print("1".isdigit())  # True
        print("1.1".isdigit())  # False
        print("-1".isdigit())  # False
        print("01".isdigit())  # True
        print("Ⅶ".isdigit())  # False
        print("一".isdigit())  # False
        print("\u00b3".isdigit())  # True
        print("\u00b3")  # ³ 上标2
        print("\uffb3".isdigit())  # False

    @staticmethod
    def test_isnumeric():
        print("a".isnumeric())  # False
        print("1".isnumeric())  # True
        print("1.1".isnumeric())  # False
        print("-1".isnumeric())  # False
        print("01".isnumeric())  # True
        print("Ⅶ".isnumeric())  # True
        print("一".isnumeric())  # True
        print("\u00b3".isnumeric())  # True

    @staticmethod
    def test_index():
        print("abc".find("d"))  # -1
        print("abca".find("a"))  # 0
        print("abca".rfind("a"))  # 3
        print("abca".rfind("a", 0, 3))  # 0
        print(" " in "a b")  # True
        print(" " in "ab")  # False

    @staticmethod
    def test_substr():
        print("abc"[3:])

    @staticmethod
    def test_strip():
        """空格和制表符都会被截断"""
        print("|%s|" % " abc	".strip())
