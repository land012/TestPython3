# coding: utf-8

import unittest


class SetDemo(unittest.TestCase):

	@staticmethod
	def test1():
	    set1 = set([1, 2, 2, 3])
	    set1.add(7)
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


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SetDemo('test2'))

    unittest.TextTestRunner(verbosity=2).run(suite)
