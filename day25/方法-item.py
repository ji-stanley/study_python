# __author__: Stanley
# date: 2018/10/22

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        return item + 10

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


obj = Foo("stnley", 25)
# 自动执行obj对象的类中的__getitem__方法。555当作参数传递
result = obj[555]
print(result)
obj[111] = 444
del obj[222]

