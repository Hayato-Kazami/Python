import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 28, 32],
    '部门': ['技术部', '销售部', '技术部', '人事部', '销售部'],
    '工资': [5000, 7000, 6000, 5500, 7500]
})

print("原始数据:")
print(df)

# 条件筛选 类似sql的where

print("年龄小于30岁的：", df[ df['年龄'] < 30 ])

# 部门是销售部
print("销售部：", df[ df['部门'] == '销售部'])

# 类SQL
print("年龄大于28且工资小于7000：\n", df.query("年龄 > 28 and 工资 < 7000"))

# 排序 order by ascending=False是降序
print("按工资排序：\n", df.sort_values('工资', ascending=False))


print("多列排序：\n", df.sort_values(['部门', '工资'], ascending=[False,True]))