import unittest

__author__ = 'xudazhou'


class UnicodeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        str1 = u'中文'
        print(str1)

        print(str1.encode(encoding="utf-8"))  # b'\xe4\xb8\xad\xe6\x96\x87'

        str1 = "\u7ec7\u7530\u4fe1\u957f"  # 织田信长
        str2 = "a"
        print(str1)
        print(str2 + str1)  # a织田信长

    @staticmethod
    def test1_1():
        bin1 = "0xa0"
        i1 = int(bin1, 16)
        print(i1)  # 160
        print(chr(i1))  # 不可见字符

    @staticmethod
    def test2():
        str3 = "\\u7ec7\\u7530\\u4fe1\\u957f"
        print(str3)  # \u7ec7\u7530\u4fe1\u957f

        str3_byte = str3.encode("utf-8")
        print(type(str3_byte))  # <class 'bytes'>
        print(str3_byte)  # b'\\u7ec7\\u7530\\u4fe1\\u957f'

        str3_par = str3_byte.decode("unicode_escape")
        print(str3_par)  # 织田信长

        print(str3_par.encode("unicode_escape"))  # b'\\u7ec7\\u7530\\u4fe1\\u957f'
        print(str3_par.encode("utf-8"))  # b'\xe7\xbb\x87\xe7\x94\xb0\xe4\xbf\xa1\xe9\x95\xbf'
