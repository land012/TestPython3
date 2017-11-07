#!/usr/bin/python
# Filename : helloworld.py

# 多行字符串
'''
print("""Hello
World""")
'''

# 单行字符串
#print("Hello \
#World")

# 不会进行转义
#print(r"newline is indicated by \n")

'''
# print 参数
print("a", "b", "c") # 默认以空格分隔
print("a", "b", "c", sep="|") # 指定关键参数sep为“|”，以“|”分隔

t1 = "a"
t2 = "b"
print(t1, t2)
'''

# 双引号
'''
t1 = "a"
print("haha=" + t1)  # haha=a
'''

print("这里是中文")

# 当前文件名
print(__file__)  # D:/_python/TestPython3/src/com/demo/helloworld/helloworld.py
cur_filename = __file__.split("/")[-1]
print(cur_filename)  # helloworld.py


