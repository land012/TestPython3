#coding:utf-8

from collections import Iterable
from collections import Iterator

__author__ = 'xudazhou'

def fib(n):
    a, b = 1, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


f = fib(5)
print(f)  # <generator object fib at 0x00000000022357E0>
print(isinstance(f, Iterable))  # True
print(isinstance(f, Iterator))  # True
print(f.__next__())  # 1

"""
1
1
2
"""
"""
for i in f:
    print(i)
"""
"""
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)  # None
        break
"""
