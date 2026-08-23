import re

def check():
    str1 = input("请输入字符串：")
    res = re.match('.*test.*', str1)
    if res:
        print("匹配成功")
        print(res.group())
        return True
    else:
        print("Fail")
    return False

check()