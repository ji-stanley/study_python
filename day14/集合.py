# __author__: Stanley
# date: 2018/3/6

# 集合天生去重,无序

# 创建集合
s = set('where')
print(s)

# 新增元素
s.add("jump") # 把字符串当成一个元素。
print(s)
s.update("is") # 把字符串分开每个去增加元素
print(s)

# 更新
s.update(["jump",'ok'])
print(s)

# 删除
s.remove("jump") # 指定数据删除
print(s)
s.pop() # 随机删除
print(s)
s.clear() # 清空数据
print(s)

# 利用集合特性去去重列表中的多余数据
userlist = ['ZhanSan','LiSi','ZhanSan']
print(set(userlist),type(set(userlist)),list(set(userlist))) # 利用set特性去重列表

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

# 交集
print(a.intersection(b))
print(a&b)

# 并集
print(a.union(b))
print(a|b)

# 差集
print(a.difference(b))
print(a-b)

# 对称差集(反向交集)
print(a.symmetric_difference(b))
print(a^b)

# 父集
print(a.issuperset(b))
print(a>b)

# 子集
print(a.issubset(b))
print(a<b)