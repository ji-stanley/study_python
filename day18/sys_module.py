# __author__: Stanley
# date: 2018/4/4

# python 解释器交互
import sys

print(sys.argv )         # 命令行参数List，第一个元素是程序本身路径
# sys.exit(1)       # 退出程序，正常退出时exit(0)
print(sys.version)       # 获取Python解释程序的版本信息
print(sys.maxsize)       # 最大的Int值
print(sys.path)        # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform )     # 返回操作系统平台名称
sys.stdout.write('please:')
