import unittest

class StringSplit(unittest.TestCase):

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
    def test_split():
        """
        默认按空白字符分割 空格和制表符都会作为分隔符
        """
        str3 = "a  b c		d"
        arr3 = str3.split()
        print(arr3)  # ['a', 'b', 'c', 'd']
        print(len(arr3))  # 4

    @staticmethod
    def test_split2():
        # 按 \t 分割字符串
        str3_2 = "a a		b			c d"
        arr3_2 = str3_2.split("\t", maxsplit=1)
        print(type(arr3_2))  # <class 'list'>
        print(len(arr3_2))  # 2
        print(arr3_2)  # ['a a', '\tb\t\t\tc d'] 空字符串会被保留
        print(arr3_2[1])  # 

    @staticmethod
    def test_split3():
        str4 = "1.2 3"
        arr4 = str4.split()
        print(float(arr4[0]) + 0.5)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(StringSplit("test3"))
    suite.addTest(StringSplit("test_split"))
    suite.addTest(StringSplit("test_split2"))

    unittest.TextTestRunner(verbosity=2).run(suite)
