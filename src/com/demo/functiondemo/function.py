#!/usr/bin/python


# 函数
def sayHello():
    print("Hello World")


#sayHello()



# 带形参的函数
#def sayHello(name):
#    print("Hello", name)

#sayHello("Tom")



# 全局变量和局部变量
# 这中写法，x 在函数中被认为是全局变量
def fn1():
    print("x is", x)
#    x = 2

# 这种写法是错误的，x 被认为是局部变量
# UnboundLocalError: local variable 'x' referenced before assignment
#def fn2():
#    print("x is", x)
#    x = 2

#x = 20
#fn1()
#print(x)


# 默认参数值
def fn3(msg, times = 1):
    print(msg * times)
# 调用有默认参数的函数
#fn3("hello")
#fn3("Hello", 2)


def fn4(msg, times):
    print(msg * times)
# 这种调用方式会报错 TypeError: fn4() missing 1 required positional argument: 'times'
#fn4("tom")

# 这种定义会报错 SyntaxError: non-default argument follows default argument
# 非默认参数 不能 在默认参数后面
#def fn5(a=1, b, c=3):
#    print("a=", a, ",b=", b, ",c=", c)


# 关键参数
def fn6(a, b=11, c=21):
    print("a=", a, ", b=", b, ", c=", c)

#fn6(1, 12)
#fn6(2, c=22)


# 模块 __name__
if __name__ == "__main__":
    print("The helloworld.py is being run by itself")
else:
    print("The helloworld.py is imported from another module")
