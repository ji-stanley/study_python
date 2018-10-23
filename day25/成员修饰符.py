# __author__: Stanley
# date: 2018/5/30

class Foo:
    __n = 1

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 双下划线__，字段称为私有成员，外部无法调用。

    # 获取私有成员的方法。
    def bar(self):
        return self.__age, Foo.__n


obj = Foo('stanley', 25)
print(obj.name)
# print(obj.__age)
# print(obj.__n)
result = obj.bar()
print(result)
