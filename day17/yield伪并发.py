# __author__: Stanley
# date: 2018/3/28

import time

def consumer(name):
    print("%s 准备吃包子啦！"%name)
    while True:
        baozi = yield
        print("包子【 %s 】来了，被【%s】吃了"%(baozi,name))


def producer(name):

    print("%s 开始做包子了"%name)
    c = consumer("张三")
    c2 = consumer("李四")
    next(c)
    next(c2)
    for i in range(10):
        time.sleep(1)
        print('%s 做了2个包子。'%name)
        c.send(i)
        c2.send(i)

producer("王二")