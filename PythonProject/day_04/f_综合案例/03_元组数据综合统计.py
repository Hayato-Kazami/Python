"""
元组数据综合统计
任务描述：定义元组 data = (78, 92, 80, 92, 66, 78, 92, 88)
1. 计算所有数据的平均分
2. 统计 92 分出现的次数
3. 查找第一个 78 出现的索引
4. 切片获取第 2 个到第 6 个元素
5. 遍历输出所有大于 80 的成绩
"""
data = (78, 92, 80, 92, 66, 78, 92, 88)

# 1. 计算所有数据的平均分
avg = sum(data) / len(data)
print(f"平均分: {avg:.2f}")

# 2. 统计 92 分出现的次数
count_92 = data.count(92)
print(f"92 分出现的次数: {count_92}")

# 3. 查找第一个 78 出现的索引
index_78 = data.index(78)
print(f"第一个 78 出现的索引: {index_78}")

# 4. 切片获取第 2 个到第 6 个元素 (索引 1~5)
slice_data = data[1:6]
print(f"第 2 个到第 6 个元素: {slice_data}")

# 5. 遍历输出所有大于 80 的成绩
print("大于 80 的成绩:", end=" ")
for score in data:
    if score > 80:
        print(score, end=" ")
print()
