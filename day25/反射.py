# __author__: Stanley
# date: 2018/10/23

"""
class Foo(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


obj = Foo("stanley",25)


# 通过字符串形式进行操作对象中的成员。
# 获取值
result = getattr(obj,"name")
print(result)

# 判断值，返回布尔
print(hasattr(obj,"name"))
print(hasattr(obj,"aa"))

#   设置值
setattr(obj,"k1","v1")
print(obj.k1)

# 删除值
delattr(obj,"name")
print(obj.name)
"""


from day25 import attrtest

inp = input(">>>：").strip()
if hasattr(attrtest,inp):
    func = getattr(attrtest,inp)
    result = func()
    print(result)
else:
    print("404")