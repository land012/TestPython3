# coding: utf-8

import unittest
import html

class HTMLParserTest(unittest.TestCase):

    @staticmethod
    def test1():
        print(html.unescape("&#x0076;&#x0069;&#x0070;&#x5728;&#x7b49;&#x4f60;"))
