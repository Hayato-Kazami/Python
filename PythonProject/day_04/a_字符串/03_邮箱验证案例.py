"""
用户输入一个邮箱，验证格式是否合法：
- 必须包含且仅包含一个 @
- 必须包含至少一个 .
满足则输出：邮箱格式正确;否则输出：邮箱格式错误
示例邮箱：heima@itcast.cn     heima@163.com    heima@google.mail.com
"""
"""
用户输入一个邮箱，验证格式是否合法：
- 必须包含且仅包含一个 @
- 必须包含至少一个 .
满足则输出：邮箱格式正确;否则输出：邮箱格式错误
示例邮箱：heima@itcast.cn     heima@163.com    heima@google.mail.com
"""

# 1. 用户输入一个邮箱 input
email = input("请输入一个邮箱:")

# 2. 判断格式是否正确
# 包含一个@ 和 至少一个.
if email.count("@") == 1 and "." in email:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
