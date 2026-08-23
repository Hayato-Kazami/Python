import re

def check_password():
    str1 = input("请输入密码：")

    if len(str1) < 8 :
        print("密码长度不足8位！")
        return False

    p = r"[a-z]"
    res = re.search(p, str1)
    if not res:
        print("必须包含小写字母！")

    p = r"[A-Z]"
    res = re.search(p, str1)
    if not res:
        print("必须包含大写字母！")

    p = r"\W"
    result = re.search(p, str1)

    if not result:
        print("必须包含特殊字符")
        return False

    print("密码设置OK")
    return True

check_password()
