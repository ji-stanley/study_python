# __author__: Stanley
# date: 2018/8/21

"""
class Foo:
    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")

obj = Foo() # 自动执行init方法。
obj() # 自动执行call方法。
"""


class Foo:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return "%s,%s" % (self.name, self.age)


obj = Foo("stanley", 25)
print(obj) # obj自动调用Foo中的str方法，获取其返回值。


class Foo1:
    def __init__(self, n, a):
        self.name = n
        self.age = a


obj1 = Foo1("stanley", 25)
print(obj1)
