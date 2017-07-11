import struct
import sys

__author__ = 'xudazhou'

i1 = 5
# int 转 字节数组
s1 = struct.pack('i', i1)
print(type(s1))  # <class 'bytes'>
print(len(s1))  # 4
print(s1) # b'\x05\x00\x00\x00'
# TypeError: must be str, not bytes
#sys.stdout.write(s1)

s2 = struct.pack('>i', i1)
print(s2) # b'\x00\x00\x00\x05'

# 字节数组 转 int
i1_1 = struct.unpack('>i', s2)[0]
print(i1_1)  # 5
