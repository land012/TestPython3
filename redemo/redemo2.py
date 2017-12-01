__author__ = 'xudazhou'

import re

# 正则表达式
# 加时间 支持到分钟
'''
从 file1 中读取字幕，读取里面的时间信息，把时间加指定 step_hseconds，然后把结果输出到 file2 中
'''

file1 = open("F:\\Download\\_新建文件夹\\プリーズ\\プリーズ・◯◯◯・ミー！ ～千鳥悠真 ピーが！ピーを？ピーされちゃった！？編～1.ass", mode="r", encoding="utf-8")

file2 = open("F:\\Download\\_新建文件夹\\プリーズ\\プリーズ・◯◯◯・ミー！ ～千鳥悠真 ピーが！ピーを？ピーされちゃった！？編～.ass", mode="w", encoding="utf-8")

pattern = re.compile(r",(\d{1}:\d{2}:\d{2}\.\d{2}),")

# 时间晚出现的秒后百进制数
step_hseconds = 290
# 时间字符串长度
group_length = 10

for line in file1:
    # print(line, end='')
    line1 = line
    mo = pattern.search(line)
    while mo:
        group1 = mo.group(1)
        pos1 = mo.start(1)
        list0 = group1.split(".")
        hseconds_o = int(list0[1])  # 秒后百进制数字
        list1 = list0[0].split(":")
        minute1_o = int(list1[1])  # 分钟
        second1_o = int(list1[2])  # 秒

        hseconds = hseconds_o + step_hseconds
        hseconds_quotient = 0  # 商
        if hseconds > 99:
            hseconds_quotient = hseconds // 100
            hseconds_remainder = hseconds % 100
            hseconds = hseconds_remainder

        second1 = second1_o + hseconds_quotient
        minute1 = minute1_o
        if second1 > 59:
            minute1 = minute1_o + 1
            second1_remainder = second1 - 60
            second1 = second1_remainder

        minuteStr1 = str(minute1)
        secondStr1 = str(second1)
        hsecondsStr = str(hseconds)

        if minute1 < 10:
            minuteStr1 = '0' + minuteStr1
        if second1 < 10:
            secondStr1 = '0' + secondStr1
        if hseconds < 10:
            hsecondsStr = '0' + hsecondsStr
        group1new = "0:" + minuteStr1 + ":" + secondStr1 + "." + hsecondsStr
        # print("%s %d %s %s" % (group1, pos1, list1, group1new), end=' | ')
        line1 = line1[0:pos1] + group1new + line1[pos1+group_length:]
        mo = pattern.search(line, pos1)
    print(line1, end='')
    file2.write(line1)

file1.close()
file2.close()
