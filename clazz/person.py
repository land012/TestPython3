#!/usr/bin/python
__author__ = '大洲'

import logging


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


class Person:
    def __init__(self):
        """python 不支持重载，这个方法不生效"""
        pass  # an empty block

    def __init__(self, name = "TOM"):
        self.name = name

    def sayhi(self):
        """
        因为没有引用 self的变量，所以代码检查这个方法可以是 static
        :return:
        """
        logging.info("Hi Leah Dizon")

    def sayhello(self):
        logging.info("Hello %s" % self.name)

    def __str__(self):
        return "I am %s" % self.name

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


if __name__ == "__main__":
    # python 不支持重载
    # 当定义有参数的 init 方法时，这种用法会报错
    # TypeError: __init__() missing 1 required positional argument: 'name'
    p1 = Person()
    p1.sayhi()
    logging.info(p1)
    logging.info(str(p1))

    p2 = Person("Alphonse")
    p2.sayhello()

    p3 = Person("Alphonse")

    logging.info(p2 == p3)  # True

    dict1 = dict()
    dict1[p2] = "alp"
    logging.info(p3 in dict1)  # True
