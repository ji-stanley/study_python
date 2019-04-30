#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date : 2019-04-30 
'''
import subprocess

ret = subprocess.Popen('lsa', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)

# poll():检查进程是否终止，如果终止返回returncode，否则返回None。
# wait(timeout):等待子进程终止。
# communicate(input,timeout):和子进程交互，发送和读取数据。
# send_signal(singnal):发送信号到子进程
# terminate():停止子进程,也就是发送SIGTERM信号到子进程。
# kill():杀死子进程。发送SIGKILL信号到子进程

ret.wait(2)
if ret.poll() == 0:
    print('success', str(ret.stdout.read(), 'utf-8'))
else:
    print('error', str(ret.stderr.read(), 'utf-8'))
'''

import socket, subprocess

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(1)

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception as  e:
            break
        if not data:
            break
        cmd_ret = subprocess.Popen(
            str(data,'utf-8'),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        cmd_ret.wait(1)
        if cmd_ret.poll() == 0:
            # 测试发现这个数据只能读取一次。
            result_data = cmd_ret.stdout.read()
            cmd_ret_len = bytes(str(len(result_data)),'utf-8')
            conn.sendall(cmd_ret_len)
            conn.sendall(result_data)
        else:
            # 测试发现这个数据只能读取一次。
            result_data = cmd_ret.stderr.read()
            cmd_ret_len = bytes(str(len(result_data)), 'utf-8')
            conn.sendall(cmd_ret_len)
            conn.sendall(result_data)
    conn.close()

sk.close()
