# __author__: Stanley
# date: 2018/3/8

# if True:
#     x=3
# print(x)

# x = int(2.3)  # built-in
# g_count = 0  # global 全局变量
#
#
def outer():
    o_count = 1  # enclosing 嵌套局部变量。
    def inner():
        nonlocal  o_count # 嵌套变量修改,关键字 nonlocal
        o_count = 5
        i_conut = 2  # local 局部变量
        print(i_conut)
        print(o_count)

    inner()


outer()


count = 10

def outer():
    global  count #  局部变量无法修改全局变量，如果要强行修改，就需要写关键字global
    count=count+1
    print(count)

outer()



