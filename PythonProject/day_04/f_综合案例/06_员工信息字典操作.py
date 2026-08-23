"""
员工信息字典操作
任务描述：
1. 定义员工字典：employee = {"name":"小红","job":"测试","salary":7000}
2. 添加键值对："dept":"技术部"
3. 修改薪资 salary 为 8500
4. 删除 job 键值对
5. 遍历输出所有员工信息
"""
# 1. 定义员工字典
employee = {"name": "小红", "job": "测试", "salary": 7000}
print(f"初始员工信息: {employee}")

# 2. 添加键值对 "dept":"技术部"
employee["dept"] = "技术部"
print(f"添加部门后: {employee}")

# 3. 修改薪资 salary 为 8500
employee["salary"] = 8500
print(f"修改薪资后: {employee}")

# 4. 删除 job 键值对
del employee["job"]
print(f"删除 job 后: {employee}")

# 5. 遍历输出所有员工信息
print("\n=== 最终员工信息 ===")
for key, value in employee.items():
    print(f"{key}: {value}")
