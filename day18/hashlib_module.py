# __author__: Stanley
# date: 2018/4/4

import hashlib

m = hashlib.md5()
print(m)


m.update('hello world'.encode('utf8'))
print(m.hexdigest()) # 打印16进制加密后的数据。
m.update('stanley'.encode('utf8'))
print(m.hexdigest())

s=hashlib.sha256()
s.update('stanley'.encode('utf-8'))
print(s.hexdigest())