#!/usr/bin/python

"""
number=5
guess = int(input("Enter an integer:"))
if guess==number:
    print("Yes!")
elif guess<number:
    print("It's a little higher than that")
else:
    print("It's a little lower than that")
print("Done")
"""

# 三元表达式 ?:
print("a" if 2 > 1 else "b")  # a
print("a" if 2 > 3 else "b")  # b
print(2 > 1 and "a" or "b")  # a
print((2 > 3 and ["a", "c"] or ["b", "d"])[1])  # d
