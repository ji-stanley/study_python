# __author__: Stanley
# date: 2018/5/3

class Father:
    def f1(self):
        print("F.f1")

    def f2(self):
        print("F.f2")

class Son(Father): # 继承父类Father
    def s1(self):
        print("S.s1")

    def f2(self):  #重写父类f2方法
        super(Son,self).f2() # 执行父类（基类）f2方法。 推荐
        # Father.f2(self) # 执行父类（基类）f2方法。
        print("S.f2")


obj = Son()

obj.s1()
obj.f2()
