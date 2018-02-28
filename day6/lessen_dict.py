# __author__: Stanley
# date: 2018/2/5

# 创建(两种方法)
# 1
# dic = {'name': 'stanley', 'age': 24, 'hobby': 'girl','is_handsome':True}
# print(dic['name'])
# # 2
# dic = dict((('name','stanley'),('age',24)))
# print(dic)

# 增
# dic1 = {'name':'stanley'}
# dic1['age'] = 20
# print(dic1)
#
# ret = dic1.setdefault('age',22)  # 意思说如果没有就增加，有返回值，存在就返回字典中对应的值
# print(ret)
# ret = dic1.setdefault('job','it')
# print(ret)
# print(dic1)

# 查
# dic2 = {'name': 'stanley', 'age': 24, 'hobby': 'girl','is_handsome':True}
# print(dic2.keys(),'-->',list(dic2.keys()))
# print(dic2.values())
# print(dic2.items(),'-->',list(dic2.items()))

# 修改
# dic3 = {'name': 'stanley', 'age': 24, 'hobby': 'girl','is_handsome':True}
# # dic3['name'] = 'lisi'
# # print(dic3)
# testdic = {'111':'222','name':'aaaa'}
# dic3.update(testdic)
# print(dic3)

# 删除
dic4 = {'name': 'stanley', 'age': 24, 'hobby': 'girl','is_handsome':True}
# del dic4['name']
# print(dic4)
# dic4.clear()
# print(dic4)
# ret =  dic4.pop('name') # 把删除的key的value返回
# print(dic4,'-->',ret)
# dic4.popitem() # 随机删除。


