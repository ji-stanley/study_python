# __author__: Stanley
# date: 2018/3/22

s = (x for x in range(5000))
# # print(s.__next__()) # 不推荐这么使用，因为双下划线是内置方法。
# print(next(s))  # 推荐这么使用。 in py2 s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# # print(next(s))  # 超出会报错。


# # 生成器是一个可迭代对象
# for i in s:
#     print(i)


# def foo():
#     yield  1
#
# print(foo)
# print(foo())
# print(next(foo()))

def bar():
    print("ok")
    conut = yield 1
    print(conut)
    yield  2

c = bar()
c.send(None) # 第一次前如果没有next，只能传一个send(None)
print("---------")
ret = c.send("aaa")
print("----------")
print(ret)

