#!/usr/bin/python
__author__ = '大洲'


class Person:
    def __init__(self):
        pass  # an empty block

    def __init__(self, name):
        self.name = name

    def sayhi(self):
        """
        因为没有引用 self的变量，所以代码检查这个方法可以是 static
        :return:
        """
        print("Hi Leah Dizon")

    def sayhello(self):
        print("Hello %s" % self.name)


if __name__ == "__main__":
    # 当定义有参数的 init 方法时，这种用法会报错
    # TypeError: __init__() missing 1 required positional argument: 'name'
    p1 = Person()
    p1.sayhi()

    p2 = Person("Alphonse")
    p2.sayhello()
