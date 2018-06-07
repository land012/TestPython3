__author__ = 'xudazhou'


str1 = u'中文'
print(str1)

print(str1.encode(encoding="utf-8"))  # b'\xe4\xb8\xad\xe6\x96\x87'

str1 = "\u7ec7\u7530\u4fe1\u957f"  # 织田信长
str2 = "a"
print(str1)
print(str2 + str1)  # a织田信长

print("================================== 1 ====================================")

str3 = "\\u7ec7\\u7530\\u4fe1\\u957f"
print(str3)  # \u7ec7\u7530\u4fe1\u957f
print(str3.encode("utf-8").decode("unicode_escape"))  # 织田信长
print("织田信长".encode("unicode_escape"))  # b'\\u7ec7\\u7530\\u4fe1\\u957f'

str3_byte = str3.encode(encoding="utf-8")
print(str3_byte)  # b'\\u7ec7\\u7530\\u4fe1\\u957f'
print(str3_byte.decode(encoding="unicode-escape"))  # 织田信长

