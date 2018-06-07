#!/usr/bin/python3.3
__author__ = 'xudazhou'

import sys

last = ""
sums = 0
for line in sys.stdin:
    word, count = line.strip().split("\t")
    if word != last:
        if sums > 0: print("%s\t%d" % (last, sums))
        last = word
        sums = int(count)
    else:
        sums += int(count)

print("%s\t%d" % (last, sums))
