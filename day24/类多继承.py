# __author__: Stanley
# date: 2018/5/3


class F1:
    def a(self):
        print("F1.a")

class F2:
    def a(self):
        print("F2.a")

# class S(F1,F2):
class S(F2,F1): # 左侧优先，如果有了同一个根，最后执行
    pass

obj = S()
obj.a()