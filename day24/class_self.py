# __author__: Stanley
# date: 2018/4/27

class Foo:
    def bar(self,msg):
        print(self.name,self.age,self.gender,msg)

u = Foo()
u.name = '李四'
u.age = 20
u.gender = '男'
u.bar("去挖煤")


u1 = Foo()
u.name = '张三'
u.age = 25
u.gender = '男'
u.bar("去跑步")