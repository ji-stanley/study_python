# __author__: Stanley
# date: 2018/3/13


# 参考连接
# http://www.runoob.com/python/python-built-in-functions.html
# https://docs.python.org/3.5/library/functions.html

# abs返回绝对值
# print(abs(-333))


# filter,过滤器的功能(可迭代对象)
s = [1,2,3,4]
def func(c):
    if c != 3:
        return c

print("正常调用返回",func(s))
ret = filter(func,s)
print(ret) # 返回的是一个迭代器
print("通过filter调用",list(ret))

#　map 修改(可迭代对象)
s = ['a1','b1','c1']

def  func_map(s):
    return  s + 'alvin'

ret = map(func_map,s)
print(ret)
print(list(ret))


# reduce
from functools import reduce

def add_reduce(x,y):
        return  x+y

print(reduce(add_reduce,range(1,5))) # 结果就是一个数值。
# 实现原理
# [1,2,3,4,]
# [3,3,4,]
# [6,4]
# 10

# lambda 匿名函数
num = lambda  a,b:a+b
print(num(1,2))

# lambda配合reduce实现阶乘
print(reduce(lambda x,y:x*y,range(1,6)))