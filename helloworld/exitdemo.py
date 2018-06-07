import sys
import os
import traceback

__author__ = 'xudazhou'

# 可以捕获到 SystemExit 异常
"""
try:
    sys.exit(0)
except SystemExit as e:
    traceback.print_exc()
    print(e)  # 0
"""

# 可以捕获到 SystemExit 异常
"""
try:
    exit(1)
except SystemExit as e:
    traceback.print_exc()
    print(e)  # 1
"""

os._exit(1)

