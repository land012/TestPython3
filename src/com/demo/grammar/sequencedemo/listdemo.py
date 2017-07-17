__author__ = 'xudazhou'

# ######################### 列表 ##########################
#shoplist = [ "apple", "mango", "carrot", "radish" ]
#print("items count:", len(shoplist)) # 列表大小
#print(shoplist)

#print("===============================")

# 遍历
#for i in shoplist:
#    print(i, end=" ")

#print()
#print("===============================")

# 下标从 0 开始
#shoplist.append("banana") # 追加记录
#print("shoplist:", shoplist)
#shoplist.sort() # 列表排序
#print("sorted shoplist:", shoplist)
#print("shoplist[0]:", shoplist[0]) # 获取指定索引记录

#olditem = shoplist[0]
#del shoplist[0] # 删除列表记录
#print("olditem:", olditem)
#print("shoplist:", shoplist)

# 可以有重复记录
#mylist = [ "history", "english", "history" ]
#print(mylist)
#print(len(mylist))
#mylist.sort()
#print(mylist)

# 列表中有字典
'''
mylist3 = []
for i in range(1, 4):
    mylist3.append({ "i" : i })

print(mylist3) # [{'i': 1}, {'i': 2}, {'i': 3}]
'''

# 空列表 不会报错
'''
list4 = []
for i in list4:
    print(i)
'''

# 下标越界的报错
list5 = [1, 2]
# 报错 下标越界
# IndexError: list assignment index out of range
#list5[2] = 3

# IndexError: list index out of range
# print(list5[2])


# 判断是否包含
list6 = ["a", "b", "c", "de"]
print("a" in list6)  # True
print("d" in list6)  # False
print(list6.reverse())  # None

# list6 已经变为逆序
for e in list6:
    print(e)

