"""
元组成绩统计
元组：scores = (77, 85, 92, 85, 69, 92, 77)
1. 求总分、平均分
2. 统计 85 出现次数
3. 查找第一个 92 的索引
4. 切片取前 5 个成绩
"""
scores = (77, 85, 92, 85, 69, 92, 77)

# 1. 求总分、平均分
total = sum(scores)
avg = total / len(scores)
print(f"总分: {total}")
print(f"平均分: {avg:.2f}")

# 2. 统计 85 出现次数
count_85 = scores.count(85)
print(f"85 出现次数: {count_85}")

# 3. 查找第一个 92 的索引
index_92 = scores.index(92)
print(f"第一个 92 的索引: {index_92}")

# 4. 切片取前 5 个成绩
first_5 = scores[:5]
print(f"前 5 个成绩: {first_5}")
