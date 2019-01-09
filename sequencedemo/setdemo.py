# coding: utf-8

import unittest


class SetDemo(unittest.TestCase):

	@staticmethod
	def test1():
	    set1 = set([1, 2, 2, 3])
	    set1.add(7)
	    print(set1)

	@staticmethod
	def test1_1():
		set1 = {1, 2, 3, 1}
		print(set1)

	@staticmethod
	def test2():
		set1 = set([1, 2])
		set2 = set([3, 4])
		set3 = set1.union(set2)
		set4 = set1 | set2
		print(set1)  # {1, 2}
		print(set3)  # {1, 2, 3, 4}
		print(set4)  # {1, 2, 3, 4}

	@staticmethod
	def test3():
		"""
		set 是无序的
		:return:
		"""
		set1 = set()
		set1.add(1)
		set1.add(2)
		set1.add(1)
		set1.add(5)
		set1.add(3)
		set1.add(4)
		set1.add(3)
		set1.add(5)
		print(set1)  # {1, 2, 3, 4, 5}


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SetDemo('test2'))

    unittest.TextTestRunner(verbosity=2).run(suite)
