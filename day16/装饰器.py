# __author__: Stanley
# date: 2018/3/15

import time


# 遵守开放封闭原则。


def show_time(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("spend %s" % (end - start))

    return inner


@show_time  # foo = show_time(foo)
def foo():
    print("foo ...")
    time.sleep(1)


foo()
