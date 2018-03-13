# __author__: Stanley
# date: 2018/3/13

def f(*args):
    print(args)


f([1,2,3]) # 成为一个单独的元素。 #　([1, 2, 3],)
f(*[1,2,3]) # 一一对应。 ＃(1, 2, 3)

def dic(**kwargs):
    print(kwargs)

# dic({'name':'stanley'})   # 这个样子传会报异常。
dic(**{'name':'stanley'}) # 传字典的方法。