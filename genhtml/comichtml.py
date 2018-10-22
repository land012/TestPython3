# coding: utf-8

"""
comic html
"""
import unittest

class ComicHtml(unittest.TestCase):

    @staticmethod
    def test1():
        for i in range(1, 221):
            # print("<img src =\"images/%03d.png\" /><hr/>" % i)
            print("<img src =\"04/%03d.jpg\" /><hr/>" % i)

    @staticmethod
    def test2():
        for i in range(1, 193):
            print("<img src =\"images/%d.jpg\" /><hr/>" % i)


def main():
    pass


if __name__ == "__main__":
    ComicHtml.test2()
