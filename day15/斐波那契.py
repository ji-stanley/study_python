# __author__: Stanley
# date: 2018/3/13

# 循环版本
def f(n):
    before = 0
    after = 1
    for i in range(n):
        # 显示斐波那契的位置数字
        ret = after + before
        before = after
        after = ret
        # 打印斐波那契序列。
        # print(before, after, end="  ")
        # before = before + after
        # after = after + before
    return after


print(f(11))


# 递归版本
def fd(n):
    if n <= 1:
        return 1
    return fd(n - 1) + fd(n - 2)


print(fd(11))
