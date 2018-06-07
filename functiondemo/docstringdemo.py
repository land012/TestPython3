__author__ = 'xudazhou'


# DocStrings
def fn7(x, y):
    """This is fn7.

    Here is detail describetion."""
    if x > y:
        return x
    else:
        return y

print(fn7(1,
          2))

# help(fn7)
'''
Help on function fn7 in module __main__:

fn7(x, y)
    This is fn7.

    Here is detail describetion.
'''

# print("=======================================")

# print(fn7.__doc__)
'''
This is fn7.

    Here is detail describetion.
'''

# print("=======================================")

# help(print)
'''
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
