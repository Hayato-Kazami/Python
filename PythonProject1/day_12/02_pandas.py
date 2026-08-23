import pandas as pd
import numpy as np

# 从字典创建DataFrame
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '工资': [5000, 7000, 6000, 8000]
}

df = pd.DataFrame(data)
print("创建的DataFrame:")
print(df)

# 从列表创建DataFrame
data_list = [
    ['张三', 25, '北京', 5000],
    ['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],
    ['赵六', 28, '深圳', 8000]
]

df2 = pd.DataFrame(data_list, columns=['姓名', '年龄', '城市', '工资'],index = ['s1','s2','s3','s4'])
print("\n从列表创建的DataFrame:")
print(df2)

print("\n使用loc选择（标签索引）:")
print(df2.loc['s1'])  # 选择一行
print(df2.loc[['s1', 's3']])  # 选择多行
print(df2.loc['s1':'s3'])  # 切片选择

print("\n使用iloc选择（位置索引）:")
print(df2.iloc[0])  # 第一行
print(df2.iloc[[0, 2]])  # 选择多行
print(df2.iloc[0:3])  # 切片选择

# 查看DataFrame基本信息
print("\nDataFrame基本信息:")
print("形状:", df.shape)
print("列名:", df.columns)
print("索引:", df.index)
print("数据类型:\n", df.dtypes)