#!/bin/python3
import urllib.parse
import unittest


class UrllibTest(unittest.TestCase):

	@staticmethod
	def test1():
		print(urllib.parse.quote("("))  # %28
		print(urllib.parse.quote("\\"))  # %5C

	@staticmethod
	def test2():
		print(urllib.parse.unquote("%2F"))  # /


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(UrllibTest('test1'))
	suite.addTest(UrllibTest("test2"))

	unittest.TextTestRunner(verbosity=2).run(suite)
