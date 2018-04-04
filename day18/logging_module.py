# __author__: Stanley
# date: 2018/4/4

import logging

# 默认设置
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

# 自定义日志
logging.basicConfig(
    level=logging.DEBUG,  # 日志级别
    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',  # 日志格式
    # datefmt='%Y-%m-%d %H:%M:%S',  # 日志时间
    # datefmt='%a,%d %b %Y %H:%M:%S',  # 日志时间
    filename='test.log',  # 日志名
    filemode='a'  # 模式，默认是a模式
)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
