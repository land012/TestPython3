# coding:utf-8
import time

__author__ = 'xudazhou'


'''
# 时间格式化
print(time) # <module 'time' (built-in)>
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2016-07-21 08:23:18
'''

'''
# 时间解析
dt1str = "2016-08-07 13:14:15"
dt1 = time.strptime(dt1str, "%Y-%m-%d %H:%M:%S")
print(dt1)  # time.struct_time(tm_year=2016, tm_mon=8, tm_mday=7, tm_hour=13, tm_min=14, tm_sec=15, tm_wday=6, tm_yday=220, tm_isdst=-1)
print(time.mktime(dt1))  # 1470546855.0
'''


# 0时区的时间
# time.struct_time(tm_year=2016, tm_mon=8, tm_mday=29, tm_hour=3, tm_min=24, tm_sec=41, tm_wday=0, tm_yday=242, tm_isdst=0)
# print(time.gmtime())


'''
# sleep 1s
# time.struct_time(tm_year=2016, tm_mon=8, tm_mday=18, tm_hour=15, tm_min=58, tm_sec=1, tm_wday=3, tm_yday=231, tm_isdst=0)
print(time.localtime())
time.sleep(1)
# time.struct_time(tm_year=2016, tm_mon=8, tm_mday=18, tm_hour=15, tm_min=58, tm_sec=2, tm_wday=3, tm_yday=231, tm_isdst=0)
print(time.localtime())
'''

'''
# 1.1403249698098964e-06
print(time.clock())
'''

"""
# 打印当前时间戳
timestamp = time.time()
# 1472454794.01881
print(timestamp)
# 时间戳转化为时间
struct_time = time.localtime(timestamp)
# 2016-08-29 15:13:14
print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))
"""

# time 相减
start = time.time()
time.sleep(3)
print("sleep %d s" % (time.time() - start))  # sleep 3 s


