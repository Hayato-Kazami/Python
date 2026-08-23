import re
while True:
    str1 = input("请输入内容：")

    result = re.match("itheima",str1)

    if result:
        print("Success")
        print(result.group())

    else:
        print("Fail")