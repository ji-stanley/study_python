# __author__: Stanley
# date: 2018/4/4

import logging
logger = logging.getLogger()

# 创建一个handler,用于写入日志文件。
fh = logging.FileHandler('test_two.log')

# 创建一个handler，用于输出控制台。
ch = logging.StreamHandler()

# 日志格式对象
formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh)
logger.addHandler(ch)
# 设置日志级别。
logger.setLevel(logging.DEBUG)

logger.debug("logger debug message")
logger.info("logger info message")
logger.warning("logger warning message")
logger.error("logger error message")
logger.critical("logger critical message")


