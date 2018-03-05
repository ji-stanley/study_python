# __author__: Stanley
# date: 2018/3/5

# 浅复制
s = [[1,2],'aa','bb']
s2 = s.copy()
s2[0][1] = 3
print(s)
print(s2)

# 深复制
import copy
a = [[1,2],'cc','dd']
a2 = copy.deepcopy(a)
a2[0][1] = 'ff'
print(a2)
print(a)