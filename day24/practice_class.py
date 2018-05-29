# __author__: Stanley
# date: 2018/5/29


'''
游戏人生程序：
    1. 创建游戏人物。
        李四，男，29，初始战斗力1900
        麻子，男，19，初始战斗力2300
        小舞，女，24，初始战斗力2000
    2. 游戏场景。
        草丛战斗，消耗200战斗力。
        自我修炼，增加100战斗力。
        多人战斗，消耗500战斗力。

'''


class Person(object):
    def __init__(self, name, age, gender, fight):
        self.name = name
        self.age = age
        self.gender = gender
        self.fight = fight

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""
        self.fight = self.fight - 200

    def practice(self):
        """ 注释：自我修炼，增加100战斗力"""
        self.fight = self.fight + 100

    def incest(self):
        """注释：多人战斗，消耗500战斗力"""
        self.fight = self.fight - 500

    def detail(self):
        """ 注释：打印当前对象详细情况。"""
        temp = "姓名：%s\n性别：%s\n年龄：%s\n战斗力：%s\n" % (self.name, self.age, self.gender, self.fight)
        print(temp)


#### 开始游戏 ####
LiSi = Person("李四", "男", 28, 1900)
MaZi = Person("麻子", "男", 19, 2300)
XiaoWu = Person("小舞", "女", 24, 2000)

LiSi.practice()  # 修炼。
XiaoWu.grassland()  # 草丛战斗
MaZi.incest()  # 多人战斗

# 打印对象详细信息。
LiSi.detail()
XiaoWu.detail()
MaZi.detail()
