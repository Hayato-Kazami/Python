"""
编写一个程序，对包含重复元素的列表进行去重，且保留元素第一次出现的顺序。
例如：已有列表：[2, 5, 3, 2, 8, 5, 1, 3]输出：{2, 5, 3, 8, 1,}
"""
org_list = [2, 5, 3, 2, 8, 5, 1, 3]

# 方式一：for +  set
target_set = set()
for e in org_list:
    target_set.add(e)

print(f"去重后的结果：{target_set}")


# 方式二：列表转集合
new_set = set(org_list)
print(f"列表转集合：{new_set}")

