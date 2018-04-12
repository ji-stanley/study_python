# __author__: Stanley
# date: 2018/4/12

import json

userinfo = {'name':'lisi','age':20}
print(type(userinfo))
data = json.dumps(userinfo)
print(type(data))

with open('json_text','w') as f:
    f.write(data)



