#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-04-30 

import socket
import re

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 8000)

sk.connect(address)

while True:
    user_cmd = input('>>>').strip()

    if user_cmd == "exit":
        break
    elif not user_cmd:
        continue
    sk.send(bytes(user_cmd, 'utf-8'))
    # data = sk.recv(1024)
    # print(str(data,'utf-8'))

    # 解决数据无法全部接收问题
    # 多次执行命令也会报错
    '''
    ValueError: invalid literal for int() with 
    base 10: '62cmd_client.py\ncmd_server.py\nsocket_client.py\nsocket_server.py\n'

    '''
    result_len = int(str(sk.recv(1024), 'utf-8'))
    print(type(result_len),result_len)
    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv
    print(str(data, 'utf-8'))

sk.close()
