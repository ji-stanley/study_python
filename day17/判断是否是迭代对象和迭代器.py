# __author__: Stanley
# date: 2018/3/29

from collections import  Iterator,Iterable

l = [1,3,4]
print(isinstance([],list))
print(isinstance(l,Iterator)) # 判断是否是迭代器。
print(isinstance(l,Iterable)) # 判断是否是可迭代对象。