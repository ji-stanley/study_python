#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-04-29 


import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP连接
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 进程间的痛惜 UNIX
# sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP连接

address = ('127.0.0.1', 8000)
# address = ('127.0.0.1', 9999)

# 绑定地址和端口
sk.bind(address)
# 可以等待的数量
sk.listen(3)

# 连接信息,conn客户端对象，addr客户端地址
# conn, addr = sk.accept()

# 发送数据，无论是接收或者发送一定要是bytes类型。
# input_str = input('>>> ').strip()
# conn.send(bytes(input_str,'utf-8'))
# conn.send(bytes('测试','utf-8'))

# # 接收数据
# data = conn.recv(1024)
# print(str(data,'utf-8'))
# # 关闭客户端
# conn.close()


# while True:
#     data = conn.recv(1024)
#     data = str(data, 'utf-8')
#     print(data)
#     if data == "exit":
#         conn.close()
#         conn, addr = sk.accept()
#         print(addr)
#         continue
#     inp = input('>>> ').strip()
#     conn.send(bytes(inp, 'utf-8'))

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception as  e:
            print('client error')
            break
        print(str(data, 'utf-8'))
        # 在客户端被强行断开的时候，会给服务端发一个空数据。
        if not data:
            print('no data')
            break
        # if str(data, 'utf-8') == "exit": break
        inp = input('>>> ')
        conn.send(bytes(inp, 'utf-8'))



sk.close()
