
max_times = 3

for i in range(max_times):
    account = input("请输入账号：")
    password = input("请输入密码：")

    if account == "admin" and password == "admin888":
        print("登录成功")
        break
    else:
        remaining = max_times - (i + 1)
        if remaining > 0:
            print(f"用户名或密码输入错误，还剩 {remaining} 次机会")
        else:
            print("用户名或密码输入错误，机会已用完")
