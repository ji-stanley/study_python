# __author__: Stanley
# date: 2018/10/22


class MyType(type):
    def __init__(self, *args, **kwargs):
        print("MyType init")

    def __call__(self, *args, **kwargs):
        print("MyType call")


class Foo(object, metaclass=MyType):
    def __init__(self):
        pass


obj = Foo()
