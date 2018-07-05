__author__ = 'xudazhou'


# NameError: name 'say_hello' is not defined
# 必须先定义，再调用
# say_hello()

# 函数
def say_hello():
    print("Hello World")


# 在函数调用时，被调用的函数，不必一定要在调用函数前面声明
def fn1():
    print("I am fn1")
    fn2()


def fn2():
    print("I am fn2")

# fn1()

def fn3(*args):
    print(type(args))  # <class 'tuple'>
    if len(args) > 0:
        print(args[0])  # a
    else:
        print("=== empty ===")

fn3()
fn3("a", "b")
