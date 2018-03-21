# __author__: Stanley
# date: 2018/3/21

import time

def logger(flag):
    def show_time(func):
        def inner(*x, **y):
            start = time.time()
            func(*x, **y)
            end = time.time()
            print("spend %s" % (end - start))
            if flag == "true":
                print("记录成功")
        return inner
    return show_time

@logger('true')  # @show_time
def add(*a,**b):
    sums = 0
    for i in a:
        sums += i
    print(sums)
    time.sleep(1)
add(1,23,4,566,9)
