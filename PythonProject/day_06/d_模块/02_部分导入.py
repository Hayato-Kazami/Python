"""
部分导入：将一个其他模块中部分内容导入到当前模块
    导入语法：from 模块名 import 成员名1[as 别名], 成员名2[as 别名],…
    使用语法：成员名
注意：
    1. 只能使用其导入的成员，未导入的成员不能使用
    2. 如果多个模块中存在重名成员，后一次导入会覆盖前一次导入，此时可以使用别名来做区分
    3. from 模块名 import * 默认导入模块中所有不以单下划线开头的成员，但是可以在被导入模块中使用__all__=[""] 明确暴露成员
"""
"""
部分导入：将一个其他模块中部分内容导入到当前模块
    导入语法：from 模块名 import 成员名1[as 别名], 成员名2[as 别名],…
    使用语法：成员名
注意：
    1. 只能使用其导入的成员，未导入的成员不能使用
    2. 如果多个模块中存在重名成员，后一次导入会覆盖前一次导入，此时可以使用别名来做区分
    3. from 模块名 import * 默认导入模块中所有不以单下划线开头的成员，但是可以在被导入模块中使用__all__=[""] 明确暴露成员
"""

# 导入语法：from 模块名 import 成员名1[as 别名], 成员名2[as 别名],…
from jisuan import name,_desc,print_module_info
# 使用语法：成员名
print(name)
# 1. 只能使用其导入的成员，未导入的成员不能使用
print(_desc)
print_module_info()




# # 2. 如果多个模块中存在重名成员，后一次导入会覆盖前一次导入，此时可以使用别名来做区分
# from calculate import name as a_mul_name
# from jisuan import name as a_add_name
#
# print(a_mul_name)
# print(a_add_name)
#
# 3. from 模块名 import * 默认导入模块中所有不以单下划线开头的成员，但是可以在被导入模块中使用__all__=[""] 明确暴露成员
# from jisuan import *
#
# print(name)
# print(_desc) # 默认导入模块中所有不以单下划线开头的成员
# print(add(1,2))