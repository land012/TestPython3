# coding: utf-8
import functools

__author__ = 'xudazhou'

def log(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **kwargs):
            print("decorator args num = %d" % len(args1))
            return func(*args2, **kwargs)

        return wrapper

    return decorator

@log("ab", "c")
def now2():
    print("i am now2")

def now3():
    print("i am now3")

# 这种注解方式没有问题
@log()
def now4():
    print("i am now4")

now2()
print("==================== 1 ========================")
"""
decorator args num = 1
i am now3
"""
log("d")(now3)()
print("==================== 2 ========================")
"""
decorator args num = 0
i am now3
"""
log()(now3)()
print("==================== 3 ========================")
"""
decorator args num = 0
i am now4
"""
now4()
print("==================== 4 ========================")
"""
会报和注释 @log 相同的错误
TypeError: decorator() missing 1 required positional argument: 'func'
所以，个人理解，python里的 装饰器注解是这么用的，它直接在注释的后面加上了 (func)

因为 log(*args) 返回的是 decorator
所以这种用法 @log 就会变成 log(func)decorator()，decorator 就会无参数传入

结果就是：
decorator()
decorator没有传入参数，所以就会报上面的错

解决办法 参考 decoratordemo3.py中的写法
"""
log(now3)()
