def login():
    correct_username = '斌子'
    correct_password = '123456'
    attempts = 3

    while attempts > 0:
        username = input("请输入账号: ")
        password = input("请输入密码: ")

        if username == correct_username and password == correct_password:
            print("登录成功！")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"用户名或密码输入错误，您还有{attempts}次机会。")
            else:
                print("用户名或密码输入错误，您已无剩余机会。")
                return

login()
