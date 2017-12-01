__author__ = 'xudazhou'

import re

# 正则表达式
# 减时间 支持到分钟

file1 = open("F:\Download\_新建文件夹\プリーズ\プリーズ・◯◯◯・ミー！ ～千鳥悠真 ピーが！ピーを？ピーされちゃった！？編～1.ass", mode="r", encoding="utf-8")

file2 = open("F:\\Download\\_新建文件夹\\プリーズ\\test.txt", "w", encoding="utf-8")

pattern = re.compile(r",(\d{1}:\d{2}:\d{2})\.")

step = 2

for line in file1:
    # print(line, end='')
    line1 = line
    mo = pattern.search(line)
    while mo:
        group1 = mo.group(1)
        pos1 = mo.start(1)
        list1 = group1.split(":")
        minute1 = int(list1[1])
        second1o = int(list1[2])
        second1 = second1o-step
        if second1<0:
            minute1 = minute1-1
            second1=60 - step + second1o
        minuteStr1 = str(minute1)
        secondStr1 = str(second1)
        if minute1<10:
            minuteStr1 = '0' + minuteStr1
        if second1<10:
            secondStr1 = '0' + secondStr1
        group1new = "0:"+minuteStr1+":"+secondStr1
        # print("%s %d %s %s" % (group1, pos1, list1, group1new), end=' | ')
        line1 = line1.replace(group1, group1new)
        mo = pattern.search(line, pos1)
    print(line1, end='')
    file2.write(line1)

file1.close()
file2.close()
