# coding: utf-8
"""
# Created by xudazhou at 2019/6/6
"""
import logging


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


class Dog:

    def wang(self):
        logging.info("wang wang")

    def wang1(self, arg1):
        f1, f2 = arg1
        logging.info("wang %s" % f1)

    def wang2(self, arg1, arg2):
        logging.info("wang %s %s" % (arg1, arg2))

    def wang3(self):
        logging.info("i am wang3")
        getattr(self, "wang1")(("a", "b"))



if __name__ == "__main__":
    dog = Dog()
    getattr(dog, "wang")  # 这种用法不会生效，没有执行 getattr
    logging.info(hasattr(dog, "wang"))  # True
    logging.info("================================")
    getattr(dog, "wang")()  # 需要加个参数，没有则是空括号
    getattr(dog, "wang1")(("tom", "lily"))
    getattr(dog, "wang2")("jim", "lucy")

    dog.wang3()
