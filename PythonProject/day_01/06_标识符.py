"""
在Python中，并不是所有的字符串都是可以作为变量名的，我们把可以做变量名的字符串称为标识符，它满足下面的规则：
    标识符只能包含字母（a-z，A-Z）、数字（0-9）、下划线（_），而且不能以数字开头
    不能使用关键字：True、False、None、and、or、if、else、elif、for、while等
    严格区分大小写，比如：age，Age，AGE是三个变量
    推荐项：见名知意，多个部分使用下划线连接（蛇形命名法），例如：user_name
"""

# 标识符只能包含字母（a-z，A-Z）、数字（0-9）、下划线（_），而且不能以数字开头
age_999 = 18
国家 = "中国"  # 不建议用中文
print(国家)

# 不能使用关键字：True、False、None、and、or、if、else、elif、for、while等
# if = "你好"

# 严格区分大小写，比如：age，Age，AGE是三个变量
age = 18
Age = 29
AGE = 30
print(age)
print(Age)

# 推荐项：见名知意，多个部分使用下划线连接（蛇形命名法），例如：user_name
user_name = "jack666@163.com"