__author__ = 'xudazhou'


str1 = "abcde"
i1 = iter(str1)

try:
    while True:
        print(i1.__next__())
except StopIteration as e:
    print("================" + str(e.value))  # ================None

print(i1)  # <str_iterator object at 0x00000000027EB5F8>


"""
g1 = (i for i in range(1, 4))
print(g1)  # <generator object <genexpr> at 0x00000000028057E0>
print(g1.__next__())  # 1
print(next(g1))  # 2
print(next(g1)) # 3
# StopIteration
print(next(g1))
"""
