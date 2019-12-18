# coding: utf-8
"""
# Created by xudazhou at 2019/6/6
"""
import hashlib

if __name__ == "__main__":
    file_path1 = r"E:\TDDOWNLOAD\run.exe"
    myhash = hashlib.md5()

    file1 = open(file_path1, mode='rb')

    # 循环读
    while True:
        b = file1.read(1024)
        if not b:
            print("====================== end")
            break
        myhash.update(b)

    # 直接读所有内容
    # myhash.update(file1.read())

    file1.close()
    print("md5:%s" % myhash.hexdigest())
