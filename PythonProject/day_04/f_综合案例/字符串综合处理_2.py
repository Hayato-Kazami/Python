"""
字符串综合处理
给定字符串：s = "  life is short i love python  "
1. 去除两端空白
2. 将 python 替换为 coding
3. 按空格分割为列表
4. 统计 is 出现次数
"""
s = "  life is short i love python  "

# 1. 去除两端空白
s = s.strip()
print(f"去除两端空白后: [{s}]")

# 2. 将 python 替换为 coding
s = s.replace("python", "coding")
print(f"替换后: {s}")

# 3. 按空格分割为列表
lst = s.split()
print(f"分割成列表: {lst}")

# 4. 统计 is 出现次数
count_is = lst.count("is")
print(f"'is' 出现次数: {count_is}")
