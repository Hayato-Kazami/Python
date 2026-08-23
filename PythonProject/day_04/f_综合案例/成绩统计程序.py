"""
成绩统计程序（进阶题）
要求：
1. 用列表保存 5 个学生姓名
2. 用列表随机生成 5 个成绩（50～100 分），和姓名一一对应
3. 计算并输出：平均分、中位数、极差、方差
4. 输出最高分同学姓名和最低分同学姓名
"""
import random

# 1. 用列表保存 5 个学生姓名
names = ["张三", "李四", "王五", "赵六", "钱七"]

# 2. 用列表随机生成 5 个成绩（50～100 分），和姓名一一对应
scores = [random.randint(50, 100) for _ in range(5)]

print("学生成绩：")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# 3. 计算统计量
avg = sum(scores) / len(scores)

sorted_scores = sorted(scores)
median = sorted_scores[len(scores) // 2]  # 5个元素的中位数

max_score = max(scores)
min_score = min(scores)
ptp = max_score - min_score  # 极差

# 方差 = Σ(x_i - avg)² / n
variance = sum((s - avg) ** 2 for s in scores) / len(scores)

print(f"\n统计结果：")
print(f"  平均分: {avg:.2f}")
print(f"  中位数: {median}")
print(f"  极差: {ptp}")
print(f"  方差: {variance:.2f}")

# 4. 输出最高分和最低分同学姓名
max_name = names[scores.index(max_score)]
min_name = names[scores.index(min_score)]
print(f"  最高分: {max_name} ({max_score}分)")
print(f"  最低分: {min_name} ({min_score}分)")
