"""
全局导入：将一个其他模块中全部内容导入到当前模块
    导入语法：import 模块名 [as 别名]
    使用语法：模块名.成员名
注意: 模块在导入的时候会自动执行里面的代码
"""
import jisuan as js
print(js.name)
print(js._desc)
print(js.add(12,6))
