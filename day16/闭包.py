# __author__: Stanley
# date: 2018/3/14

def outer():
    x = 10
    def inner():
        print(x)
    return  inner

f = outer()
f()  # 这个就闭包