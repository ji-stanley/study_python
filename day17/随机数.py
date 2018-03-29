# __author__: Stanley
# date: 2018/3/29

import random


# print(random.random()) # 显示0-1的随机数
# print(random.randint(1,8)) # 自定义显示整型随机数。
# print(random.choice('hello')) # # 自定义显示随机字符串。可以放列表，元组,不可放字典。
# a = [1,2,4,5]
# print(random.sample(a,2)) # 从序列中，选出两个随机数
# print(random.randrange(1,4)) # 不包含4

def v_code():
    code = ""
    for i in range(5):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(add)
    print(code)


v_code()
