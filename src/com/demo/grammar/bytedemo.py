__author__ = 'xudazhou'

b1 = b"hello"
print(type(b1))  # <class 'bytes'>
str1 = str(b1, encoding='utf-8')
print(type(str1))  # <class 'str'>
print(str1)

print("================== 1 ====================")

b2 = str1.encode(encoding='gbk')
str2 = b2.decode(encoding='gbk')
print(type(b2))  # <class 'bytes'>
print(b2)  # b'hello'
print(type(str2))  # <class 'str'>
print(str2)  # hello

print("================= 2 =====================")

b3 = "中文".encode(encoding='utf-8')
print(b3)  # b'\xe4\xb8\xad\xe6\x96\x87'
print(b3[0])  # 228
