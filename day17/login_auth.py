# __author__: Stanley
# date: 2018/3/22

user,pwd = 'stanley',123


def auth(auth_type):
    def login(func):
        def inner():
            if auth_type == "local":
                username = input("username：").strip()
                password = input("password：").strip()
                if username == user and int(password) == pwd:
                    print("本地验证成功 ")
                    func()
            elif auth_type == "remote":
                print("远程验证成功")
                func()
        return  inner
    return login

@auth(auth_type='local') # home = login(home)
def home():
    print('welcome to home page.')

@auth(auth_type='remote')
def finance():
    print('welcome to finance page.')

def book():
    print("welcome to book page.")

finance()
home()
