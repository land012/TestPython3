__author__ = 'xudazhou'

def num_seq():
    """get 2, 3, 4, 5, 6 ..."""
    i1 = 2
    while True:
        yield i1
        i1 += 1

"""
for i in num_seq():
    if i < 5:
        print(i)
    else:
        break
"""

# 如果不用 lamba，怎么处理这种传入两个参数的情形
def is_div(n):
    return lambda x : x % n > 0

def get_prime():
    itr = num_seq()
    while True:
        n = itr.__next__()
        yield n
        itr = filter(is_div(n), itr)


if __name__ == "__main__":
    for i in get_prime():
        if i < 14:
            print(i, end=",")
        else:
            print()
            break
