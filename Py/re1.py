import re

def main():
    while True:
        str1 = input("请输入字符串：")

        s = r"\D\d."

        res = re.match(s, str1)

        if res:
            print("匹配成功")
            print("匹配结果：", res.group())
        else:
            print("匹配失败")

if __name__ == "__main__":
    main()