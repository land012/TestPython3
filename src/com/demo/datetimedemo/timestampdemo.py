__author__ = 'xudazhou'

import datetime

now = datetime.datetime.now()
print(now)
print(now.timestamp())  # 1482142151.310688
print(now.microsecond)  # 310688
print(now.timestamp() * 1000)
print(int(now.timestamp() * 1000))
