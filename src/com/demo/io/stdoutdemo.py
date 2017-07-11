import sys

__author__ = 'xudazhou'

sys.stdout.write("a")  # a

sys.stdout.buffer.write("a".encode(encoding="utf-8")) # a
