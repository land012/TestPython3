
import time
import datetime


'''
print(datetime) # <module 'datetime' from 'D:\\ProgramDev\\Python34\\lib\\datetime.py'>
print(datetime.date) # <class 'datetime.date'>
print(datetime.time) # <class 'datetime.time'>
print(datetime.datetime) # <class 'datetime.datetime'>
'''

# datetime.date
# today = datetime.date.today()
# print(today)  # 2017-01-22
# print(today.day)  # 22
# print(today.weekday())  # 6 周日
# print(today.strftime("%Y-%m-%d")) # 2016-07-21

'''
print(datetime.datetime.today().hour)  # 11
'''

print(datetime.datetime.today().date())
# print(datetime.datetime.date())

dt1 = datetime.datetime(2017,3,29,12,00,1)
print(dt1)

'''
# 时间戳转化为日期
# 2016-08-29 15:13:14
timestamp1 = 1472454794
# 2016-08-29 07:13:14
print(datetime.datetime.utcfromtimestamp(timestamp1))
# 2016-08-29 15:13:14
print(datetime.datetime.fromtimestamp(timestamp1))
'''

# 日期解析
'''
dt1_str = "2017-01-08 15:03:45"  # 周日
dt1 = datetime.datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S")
print(dt1)
print(dt1.weekday())  # 6
'''
