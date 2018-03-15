# __author__: Stanley
# date: 2018/3/15

import time


# 遵守开放封闭原则。

def foo():
    print("foo ...")
    time.sleep(1)


def show_time(func):
    start = time.time()
    func()
    end = time.time()
    print("spend %s" % (end - start))


show_time(foo)
