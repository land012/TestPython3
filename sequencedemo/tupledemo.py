__author__ = 'xudazhou'

"""
Tuple 元组
下标从 0 开始
"""


# ######################### 元组 ##########################
zoo = ("wolf", "elephant", "penguin")
new_zoo = ("dolphin", "lion", zoo)
#print("zoo count:", len(zoo))
#print("new_zoo count:", len(new_zoo))
print("new_zoo:", new_zoo)  # new_zoo: ('dolphin', 'lion', ('wolf', 'elephant', 'penguin'))
#print("new_zoo[2]:", new_zoo[2])
#print("new_zoo[2][2]:", new_zoo[2][2])

# 只有一个元素的元组
#orchard = ("apple", )
#print("orchard:", orchard)
#print("orchard count:", len(orchard))

# 占位符打印
#name = "tom"
#age = 15
#print("%s is %d year old"%(name, age))
#print("%s is boy"%name)
