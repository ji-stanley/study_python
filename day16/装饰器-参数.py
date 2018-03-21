# __author__: Stanley
# date: 2018/3/21
import time

def show_time(func):
    def inner(*x,**y):
        start = time.time()
        func(*x,**y)
        end = time.time()
        print("spend %s" % (end - start))

    return inner


@show_time  # foo = show_time(foo)
def add(*a,**b):
    sums = 0
    for i in a:
        sums += i
    print(sums)
    time.sleep(1)

add(1,2,3,4)

