# __author__: Stanley
# date: 2018/10/23

class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v


obj = Foo.get_instance()
print(obj)


# class Foo:
#     __v = None
#
#     def get_instance(self):
#         if self.__v:
#             return self.__v
#         else:
#             self.__v = Foo()
#             return self.__v
#
#
# obj = Foo()
# print(obj.get_instance())

## 封装
# class F1:
#     def __init__(self):
#         self.name = 123
#
#
# class F2:
#     def __init__(self, a):
#         self.ff = a
#
#
# class F3:
#     def __init__(self, b):
#         self.dd = b
#
#
# f1 = F1()
# f2 = F2(f1)
# f3 = F3(f2)
#
# print(f1.name)
# print(f2.ff.name)
# print(f3.dd.ff.name)