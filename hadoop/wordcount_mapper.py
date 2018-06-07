#!/usr/bin/python3.3
__author__ = 'xudazhou'

import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print("%s%s%d" % (word, '\t', 1))
