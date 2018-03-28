# __author__: Stanley
# date: 2018/3/28


def fib(count):
    n, before, after = 0, 0, 1
    while n < count:
        yield  after
        before,after = after,after+before
        n += 1



f = fib(5)

for i in f:
    print(i)