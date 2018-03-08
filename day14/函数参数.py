# __author__: Stanley
# date: 2018/3/8

def info(name, age, sex='male'):
    print("Name: %s" % (name))
    print("Age: %s" % (age))
    print("Sex: %s" % (sex))


# 必须参数
info("stanley", 20)
# 关键字参数
info(age=30, name="lisi")
# 默认参数(跟在其他参数后边),修改默认参数
info("wanger", 20, "female")


# 不定长参数*args(无命名)，接收的是元组
def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(1, 3, 5, 6, 6, 7)

#不定长参数**kwagrs(键值对，放在*args后边)，接收的是字典
def user_info(**kwargs):
    print(kwargs)
    print("Name: %s"%(kwargs["name"]))
    print("Age: %s"%(kwargs["age"]))

user_info(name="stanley",age=24)