# __author__: Stanley
# date: 2018/3/28

# 生成器都是迭代器，迭代器不一定是生成器。

l = [1,2,3,5]
d = iter(l)
print(d)  # <list_iterator object at 0x0000010D88184DD8>

# 迭代器（两个条件）
# 1.有inter方法。
# 2.有next方法。


# for 循环内部三件事：
# 1.调用可以迭代对象的iter方法，返回一个迭代器对象
# 2.不断调用迭代器对象的next方法。
# 3.捕获迭代器异常，进行处理stopiteration。
for i in d:
    print(i)

