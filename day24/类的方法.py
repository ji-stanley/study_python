# __author__: Stanley
# date: 2018/5/29

class Foo:
    def bar(self):
        print("bar")

    @staticmethod
    def ststic():
        print("static")

    @staticmethod
    def staticfunc(i,n):
        print(i,n)

    @classmethod
    def classmd(cls):
        print("classmd")

# 普通方法：保存在对象中，由对象调用。
f = Foo()
f.bar()


# 静态方法：保存在类中，由类直接调用。
Foo.ststic()
Foo.staticfunc(1,2)


# 类方法：保存在类中，由类直接调用。
# cls ==> 当前类
Foo.classmd()


