__author__ = 'xudazhou'

import sys
import getopt

# 处理请求参数
# 请求参数; --l1=vl1 --l2 vl2 --l3 -a haha1 haha2
opts, args = getopt.getopt(sys.argv[1:], "a", ["l1=", "l2=", "l3"])

print(opts)
print(args)
