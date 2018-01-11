# coding: utf-8
"""
字符串连接执行速度
"""
import time
__author__ = 'Administrator'


if __name__ == "__main__":
    s1 = time.time()
    print(s1)

    for i in range(10000000):
        sx = "aaa%d" % i

    s2 = time.time()
    print("格式化:" + str(s2 - s1))  # 最快

    for i in range(10000000):
        sx = "aaa{0}".format(i)

    s3 = time.time()
    print("格式化2:" + str(s3 - s2))  # 最慢

    for i in range(10000000):
        sx = "aaa" + str(i)

    s4 = time.time()
    print("类型转换:" + str(s4 - s3))  # 第二快

    for i in range(10000000):
        sx = "%s %d" % ("aaa", i)

    s5 = time.time()
    print("类型转换:" + str(s5 - s4))  # 第二快
