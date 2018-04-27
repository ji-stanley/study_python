# __author__: Stanley
# date: 2018/4/24

import shelve

f = shelve.open('shelve_text')

# 写入数据
# f['info'] = {
#     'name': 'lisi',
#     'age': '18',
# }

# 获取数据
data = f.get('aa',default=0)
print(data)
