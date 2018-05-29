# __author__: Stanley
# date: 2018/5/29

class Province:
    # 静态字段属于类
    country = "中国"

    def __init__(self,name):
        # 普通字段，属于对象
        self.name = name


# 静态字段
print(Province.country)

# 普通字段
henan = Province("河南")
print(henan.name)
