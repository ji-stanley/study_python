# __author__: Stanley
# date: 2018/3/13

# 阶乘
# 普通方法
def f(n):
    ret = 1
    for i in range(1,n+1):
        ret = ret * i
    return  ret

num = f(50)
print(num)

# 递归方法
# 递归特性：
#  1.调用自身函数。
#  2.有一个明确结束条件。
#  3.递归效率低
def fact(n):
    if n == 1:
        return 1
    return  n*fact(n-1)
print(fact(50))














