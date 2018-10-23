# __author__: Stanley
# date: 2018/10/22

"""
try:
    # 主动异常关键字raise
    raise Exception("error 11 ")
except Exception as e:
    print(e)
"""

def db():
    return  False

def index():
    try:
        result = db()
        if not result:
            raise Exception("数据库异常")
    except Exception as e:
        print(e)

index()


# 自定义错误
class Se(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return  self.msg

try:
    raise Se("自定义错误")
except Se as e:
    print(e)

