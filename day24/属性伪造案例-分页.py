# __author__: Stanley
# date: 2018/5/30


page_list = [i for i in range(1000)]


class PageAction:
    def __init__(self, inputpage):
        try:
            self.page = int(inputpage)
        except Exception as e:
            self.page = 1

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val


while True:
    p = input("请输入页码：").strip()
    obj = PageAction(p)
    print(page_list[obj.start:obj.end])