"""
字典基础操作
字典：person = {"name":"小李", "age":20, "score":82}
1. 添加键值对 "gender":"男"
2. 修改 score 为 90
3. 删除 age
4. 遍历输出所有键值对
"""
person = {"name": "小李", "age": 20, "score": 82}
print(f"初始字典: {person}")

# 1. 添加键值对 "gender":"男"
person["gender"] = "男"
print(f"添加 gender 后: {person}")

# 2. 修改 score 为 90
person["score"] = 90
print(f"修改 score 后: {person}")

# 3. 删除 age
del person["age"]
print(f"删除 age 后: {person}")

# 4. 遍历输出所有键值对
print("\n最终员工信息：")
for key, value in person.items():
    print(f"  {key}: {value}")
