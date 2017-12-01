#!/usr/bin/python
# __author__ = '大洲'

import os


# 创建目录
path1 = "D:\\_python\\a"
num1 = 100
if not os.path.exists(path1):
    os.mkdir(path1)
    print("路径不存在%s %d，创建路径"%(path1, num1))
else:
    print("路径已经存在了")

# 执行操作系统命令
print(os.system("echo %cd%"))  # D:\_python\TestProj
