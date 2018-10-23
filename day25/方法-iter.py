# __author__: Stanley
# date: 2018/10/22

class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([1,2,3,4,5])

li = Foo("stanley",25)
# 如果类中有__iter__方法，对象==>可迭代对象。
# 对象.__iter__()的返回值：迭代器。

for item in li:
    print(item)




