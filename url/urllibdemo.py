#!/bin/python3
import urllib.parse
import unittest
import urllib.request as req


class UrllibTest(unittest.TestCase):

	@staticmethod
	def test1():
		print(urllib.parse.quote("("))  # %28
		print(urllib.parse.quote("\\"))  # %5C

	@staticmethod
	def test2():
		print(urllib.parse.unquote("%2F"))  # /

	@staticmethod
	def test3():
		resp = req.urlopen("http://www.baidu.com")
		res = resp.read()
		print(type(res))  # <class 'bytes'>
		res_str = str(res, encoding="utf-8")
		print(type(res_str))  # <class 'str'>
		res_str2 = res.decode(encoding="utf-8")
		print(type(res_str2))  # <class 'str'>
		print(res_str2)


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(UrllibTest('test1'))
	suite.addTest(UrllibTest("test2"))

	unittest.TextTestRunner(verbosity=2).run(suite)
