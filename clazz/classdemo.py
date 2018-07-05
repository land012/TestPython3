__author__ = 'xudazhou'

import person

p1 = person.Person("tom")
p1.sayhi()

"""
python 不支持重载
TypeError: __init__() missing 1 required positional argument: 'name'
"""
# p2 = person.Person()
# p2.name = "jim"
# p2.sayhi()
