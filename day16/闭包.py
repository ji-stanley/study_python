# __author__: Stanley
# date: 2018/3/14

def outer():
    x = 10
    def inner():
        print(x)
    return  inner

f = outer()
f()  # 这个就闭包，
# 定义：如果在一个内部的函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数被认为是闭包（closure）