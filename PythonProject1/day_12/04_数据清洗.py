# import pandas as pd
#
# # 读取csv
# df = pd.read_csv(
#     r"清洗数据.csv",         # 被读取文件路径
#     sep=",",           # 分隔符
#     engine="python",    # 指定pandas运行在python中
# )
#
# print(df)
#
#
# print("\n缺失值统计")
# print(df.isnull().sum())
# print("\n非缺失值统计")
# print(df.notnull().sum())
#
# print("\n删除含有缺失值的行")
# print(df.dropna())      # 默认df不可变，对其的修改会返回新的，原始不变
#
# # 如果想要原始的df被修改，在操作方法中添加inplace=True
# # df.dropna(inplace=True)
# # print(df)
#
# print("\n删除一行全部是缺失值的行")
# print(df.dropna(how='all'))      # 默认df不可变，对其的修改会返回新的，原始不变
#
# # 填充缺失值
# print("\n填充缺失值")
# print(df.fillna(0))
#
# print("\n均值填充")
# print(df.fillna(df.mean()))
#
# print("\n最大填充")
# print(df.fillna(df.max()))
#
# print("\n最小填充")
# print(df.fillna(df.min()))

import pandas as pd

df = pd.read_csv(r"products.csv", sep=",", engine="python")
print(df)

# 分组统计 group by + 聚合
# group by 自营非自营 sum price
# df.groupby(列)[列].sum  .mean  .min .max
df2 = df.groupby('is_self')['price'].sum()
print(df2)

# 多列分组 按是否自营和类别ID多列分组，计算求和和平均
df3 = df.groupby(['is_self', 'category_id'])['price'].agg(['sum', 'mean', 'count', 'min', 'max'])
print(df3)