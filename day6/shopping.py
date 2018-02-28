# __author__: Stanley
# date: 2018/2/5

product_list = [
    ('mac', 9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 105),
    ('bike', 2000),
]

saving = input("please input your saving:")
if saving.isdigit():
    saving = int(saving)
else:
    exit("input not digit")

while True:

    for i, v in enumerate(product_list):
        print(i, v[0])
    choice = input("选择购买商品编号[ 退出: q ]：")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(product_list):
            print(product_list[choice])
        else:
            print("编码错误")
    elif choice == "q":
        print("退出")
    else:
        print("invalid input")
