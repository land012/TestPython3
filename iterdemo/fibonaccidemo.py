# coding: utf-8
"""
# Created by xudazhou at 2019/9/19
"""

class Fibonacci:

    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self.next()

    def next(self):
        if self.n < self.max:
            r = self.b
            self.b = self.a + self.b
            self.a = r
            self.n += 1
            return r
        raise StopIteration


if __name__ == "__main__":
    fib = Fibonacci(5)
    for i in range(5):
        print(fib.next())
