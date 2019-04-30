#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-04-29 

import socket

sk = socket.socket()

# 连接server端
server_addr = ('127.0.0.1', 8000)
# server_addr = ('127.0.0.1', 9999)
sk.connect(server_addr)

# 接收数据
# data = sk.recv(1024)
# # print(data)
# print(str(data,'utf-8'))

# 发送数据
# sk.send(bytes('test', 'utf-8'))
#
# # 关闭连接
# sk.close()pycharm中同时运行多个.py文件


while True:
    inp = input('>>>')
    if inp == 'exit': break
    sk.send(bytes(inp, 'utf-8'))
    data = sk.recv(1024)
    print(str(data, 'utf-8'))

sk.close()

