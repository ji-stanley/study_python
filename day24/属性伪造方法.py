# __author__: Stanley
# date: 2018/5/30

class Foo:
    @property
    def per(self):
        return True

    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        print(111)


obj = Foo()

# @property
result = obj.per
print(result)

# @per.setter
obj.per = 666

# @per.deleter
del obj.per
