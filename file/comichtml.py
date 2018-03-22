# coding: utf-8

"""
comic html
"""
import unittest

class ComicHtml(unittest.TestCase):

    @staticmethod
    def test1():
        for i in range(1, 1172):
            print("<img src =\"images/%04d.jpg\" /><hr/>" % i)

    @staticmethod
    def test2():
        for i in range(0, 629):
            print("<img src =\"images/%d.jpg\" />\n<hr/>" % i)


def main():
    pass


if __name__ == "__main__":
    main()
