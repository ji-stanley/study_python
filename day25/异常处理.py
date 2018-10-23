# __author__: Stanley
# date: 2018/10/22


try:
    # inp = input("请输入数字：")
    inp = "12"
    # inp = "12sa"
    i = int(inp)
    # li = [11,2,3,4,5]
    # li[99]
except ValueError as e:
    print("ValueError",e)
except IndexError as e:
    print("IndexError",e)
except Exception as e:
    print("Exception",e)
else:
    print("else，没有出错执行")
finally:
    print("不管出错不出错都最后执行这个")
