"""
find(子元素)	查找子串第一次出现的索引，找不到返回 -1
count(子元素)	统计子串出现的次数
upper()	全部字母转为大写
lower()	全部字母转为小写
split()	按指定分隔符将字符串切分为列表
strip()	去除字符串两端空白字符
replace(旧元素，新元素)	将指定子串替换为新内容
startswith(子元素)	判断是否以指定子串开头，返回布尔值
endswith(子元素)	判断是否以指定子串结尾，返回布尔值
"""
"""
find(子元素)   查找子串第一次出现的索引，找不到返回 -1
count(子元素)  统计子串出现的次数
upper() 全部字母转为大写
lower() 全部字母转为小写
split() 按指定分隔符将字符串切分为列表
strip() 去除字符串两端空白字符
replace(旧元素，新元素)    将指定子串替换为新内容
startswith(子元素) 判断是否以指定子串开头，返回布尔值
endswith(子元素)   判断是否以指定子串结尾，返回布尔值
"""

# 定义字符串
str1 = "Hello World"
print(str1[6])  # W （正向索引）
print(str1[-5]) # W （反向索引）
print(str1[0:5:1]) # Hello （支持切片）
print("--------")

# find(子元素) 查找子串第一次出现的索引，找不到返回 -1
print(str1.find("W")) # 6
print(str1.find("a")) # -1
print(str1.find("aasdf")) # -1
print("--------")

# count(子元素)    统计子串出现的次数
print(str1.count("l")) # 3
print("--------")

# upper()   全部字母转为大写
print(str1.upper()) # HELLO WORLD
# lower()   全部字母转为小写
print(str1.lower()) # hello world
print("--------")

# split()   按指定分隔符将字符串切分为列表
str2 = "Hello|你好|萨瓦迪卡"
lst = str2.split("|")
print(lst,type(lst))
print("--------")


# strip()   去除字符串两端空白字符
str3="     你好      "
print(str3)
print(str3.strip())
print("--------")

# replace(旧元素，新元素)  将指定子串替换为新内容
str4 = "Hello World"
str5 = str4.replace("World","世界")
print(str4)
print(str5)
print("--------")

# startswith(子元素)   判断是否以指定子串开头，返回布尔值
print(str4.startswith("Hello")) # True
print(str4.startswith("hello")) # False

# endswith(子元素) 判断是否以指定子串结尾，返回布尔值
print(str4.endswith("World")) # True
print(str4.endswith("world")) # False