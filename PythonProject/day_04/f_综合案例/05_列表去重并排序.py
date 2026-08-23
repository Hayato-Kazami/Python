"""
列表去重并排序
任务描述：给定列表 nums = [9,3,7,3,9,2,5,7,1,2]
1. 利用集合特性对列表去重
2. 将去重后的数据转为列表
3. 对列表进行升序排序
4. 输出最终结果
"""
nums = [9, 3, 7, 3, 9, 2, 5, 7, 1, 2]

# 1. 利用集合特性对列表去重
nums_set = set(nums)
print(f"转为集合去重: {nums_set}")

# 2. 将去重后的数据转为列表
nums_unique = list(nums_set)
print(f"转回列表: {nums_unique}")

# 3. 对列表进行升序排序
nums_unique.sort() #返回None
print(f"升序排序后: {nums_unique.sort()}")

# 4. 输出最终结果
print(f"\n=== 最终结果 ===\n{nums_unique}")

# --- 另一种更简洁的写法 ---
result = sorted(list(set(nums)))
print(f"简洁写法结果: {result}")
