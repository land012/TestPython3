__author__ = 'xudazhou'

import datetime

dt1 = datetime.datetime.today()
print(dt1)

dt2 = dt1 + datetime.timedelta(days = -1)
print(dt2)
print(dt2.strftime("%Y-%m-%d %H:00:00"))  # 2016-12-15 10:00:00