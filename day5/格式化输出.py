# __author__: Stanley
# date: 2018/2/5

name = input("Name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

if salary.isdigit(): # 判断是否为数字。
    salary = int(salary)
else:
    exit("must input digit") # 退出程序

msg = """
--- info %s ---
name: %s
age : %s
job : %s
salary: %s
--- end ---
"""%(name,name,age,job,salary)
print(msg)
