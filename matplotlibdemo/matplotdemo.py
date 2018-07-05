
from numpy import *
import matplotlib
import matplotlib.pyplot as plt


def main():
	arr1 = array([[1, 2], [2, 2], [3, 4]])
	label1 = [1, 2, 1]
	print(type(arr1[:, 0]))
	# print(arr1)
	mat1 = mat(arr1)
	# print(mat1)

	# fig = plt.figure()
	# ax = fig.add_subplot(111)
	print(type(mat1[:, 0]))
	print(type(mat1[:, 0].tolist()))

	# 下面两种写法都可以画图
	# plt.scatter(mat1[:, 0].tolist(), mat1[:, 1].tolist())
	plt.scatter(arr1[:, 0], arr1[:, 1], 20, array(label1))
	plt.show()



if __name__ == "__main__":
	main()
