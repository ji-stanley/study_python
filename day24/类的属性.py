# __author__: Stanley
# date: 2018/5/29

class Foo:
    @property
    def per(self):
        return  "abc"

obj = Foo()
result = obj.per
print(result)
