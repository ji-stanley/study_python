# __author__: Stanley
# date: 2018/3/13


# 函数名可以赋值。
# 函数名可以做为函数参数，还可以做为函数的返回值。



def f(n):
    return n * n


print(f(3))


def foo(a, b, func):
    return func(a) + func(b)


result = foo(4, 5, f)
print(result)


def bar():
    def inner():
        return 8

    return inner


a = bar()
print(a(), a)
