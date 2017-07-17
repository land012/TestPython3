# coding : utf-8

from collections import Iterator

__author__ = 'xudazhou'

def squ(x):
    if x % 2 != 0:
        return x * x

list1 = [ 1, 2, 3 ]
m1 = map(squ, list1)

print(m1)  # <map object at 0x00000000027FB780>
print(type(m1))  # <class 'map'>
print(isinstance(m1, Iterator))  # True

"""
1
None
9
"""
for v in m1:
    print(v)

