# coding: utf-8

"""
comic html
"""
import unittest

class ComicHtml(unittest.TestCase):

    @staticmethod
    def test1():
        for i in range(1, 436):
            # print("<img src =\"images/%03d.png\" /><hr/>" % i)
            print("<img src =\"05/%03d.jpg\" /><hr/>" % i)

    @staticmethod
    def test2():
        for i in range(1, 195):
            print("<img src =\"4/%d.png\" /><hr/>" % i)


def main():
    pass


if __name__ == "__main__":
    ComicHtml.test1()
