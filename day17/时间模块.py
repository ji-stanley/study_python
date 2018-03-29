# __author__: Stanley
# date: 2018/3/29

import time
# print(help(time))

print(time.time()) # 打印时间戳
# time.sleep(1) # 程序休眠1秒钟
print(time.localtime()) # 结构化显示本地时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # 格式化（字符串）显示时间。
testtime = time.strptime('2018-03-29 16:29:19','%Y-%m-%d %H:%M:%S') # 把格式化后的子串转为结构化时间（需要一一对应上）。
print(testtime)
print(testtime.tm_wday) # 取出结构化时间里的周几

print(time.ctime(11))  # 在里边写时间戳就会把时间戳转换成可视化的时间
print(time.mktime(time.localtime()))  # 把本地时间转换成时间戳。


import datetime
print(datetime.datetime.now())
