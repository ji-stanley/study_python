# __author__: Stanley
# date: 2018/10/22

#
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj = Foo("stanley",25)
# 对象中封装的所有内容通过字典的形式返回。
d = obj.__dict__
print(d,type(d))
