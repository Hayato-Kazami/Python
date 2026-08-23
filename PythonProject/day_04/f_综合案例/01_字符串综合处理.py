"""
字符串综合处理
任务描述：给定字符串 s = "  I like learning Python Python very much  "
1. 去除字符串两端空白字符
2. 将所有 Python 替换为 Go
3. 按空格将字符串分割成列表
4. 统计列表中 like 出现的次数
5. 输出处理后的字符串与统计结果
"""
s = "  I like learning Python Python very much  "

# 1. 去除字符串两端空白字符
s = s.strip()
print(f"去除两端空白后: {s}")

# 2. 将所有 Python 替换为 Go
s = s.replace("Python", "Go")
print(f"替换 Python -> Go 后: {s}")

# 3. 按空格将字符串分割成列表
word_list = s.split(" ")
print(f"按空格分割成列表: {word_list}")

# 4. 统计列表中 like 出现的次数
like_count = word_list.count("like")
print(f"列表中 'like' 出现的次数: {like_count}")

# 5. 输出处理后的字符串与统计结果
print(f"\n=== 最终结果 ===")
print(f"处理后的字符串: {s}")
print(f"'like' 出现次数: {like_count}")
