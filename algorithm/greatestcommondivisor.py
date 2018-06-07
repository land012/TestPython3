__author__ = 'xudazhou'

'''
最大公约数算法
欧几里德算法/辗转相除法
'''

def getgreatestcommondivisor(list1):
    if len(list1) == 0:
        return None

    # 找到最小的元素
    minn = list1[0]
    for i in list1:
        if i < minn:
            minn = i

    # 最小的元素递减，直到可以被所有元素整除
    while True:
        iscommon = True
        for i in list1:
            if i % minn != 0:
                iscommon = False
                break
        if iscommon:
            break
        minn -= 1

    return minn


if __name__ == "__main__":
    print(getgreatestcommondivisor([1,2,3]))  # 1
    print(getgreatestcommondivisor([6, 9]))  # 3
    print(getgreatestcommondivisor([6, 12]))  # 6

    print(getgreatestcommondivisor([6, 9, 12]))  # 3