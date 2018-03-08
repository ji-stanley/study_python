# __author__: Stanley
# date: 2018/3/8


def f():
    print("ok")
    return 10 # 结束函数，返回某对象


# 先执行print然后10赋值给a。
a = f()
print(a)

# 1.如果函数没有return，默认返回None。
# 2.如果return多个对象，python会把这个封装成一个元组。