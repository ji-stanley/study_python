# __author__: Stanley
# date: 2018/4/27

class Person(object):
    def __init__(self,name,age):
        """
        构造方法,构造方法的特性，自动执行。
        :param name: 
        :param age: 
        """
        self.name = name
        self.age = age
        self.x = "o"

    def show(self):
        print("%s %s %s"%(self.name,self.age,self.x))


lisi =  Person("李四",26)
lisi.show()

wanger = Person("王二",36)
wanger.show()