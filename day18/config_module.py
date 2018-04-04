# __author__: Stanley
# date: 2018/4/4

import configparser

config = configparser.ConfigParser()

# 生成文件代码
# config["DEFAULT"] = {
#     'ServerAliveInterval': '45',
#     'Compression': 'yes',
#     'CompressionLevel': '9'
# }
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'yes'
# config["DEFAULT"]['ForwardX11'] = 'yes'
#
#
# with open('example.ini','w') as configfile:
#     config.write(configfile)


# 读取配置文件
config.read('example.ini')
print(config.sections())

# 删除部分配置文件
# config.remove_section('topsecret.server.com')