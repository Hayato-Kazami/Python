"""
1. 定义一个学生字典，包含：姓名、学号、成绩、班级
2. 添加一个键值对：'is_pass': True
3. 修改成绩为 95
4. 删除班级信息
5. 遍历输出所有键值对
"""
"""
1. 定义一个学生字典，包含：姓名、学号、成绩、班级
2. 添加一个键值对：'is_pass': True
3. 修改成绩为 95
4. 删除班级信息
5. 遍历输出所有键值对
"""
# 1. 定义学生字典
student = {"name": "张三",
           "id": "2025001",
           "score": 88,
           "class": "Python一班"}

# 2. 添加键值对
student["is_pass"] = True
# 3. 修改成绩
student["score"] = 95
# 4. 删除班级
del student["class"]

# 5. 遍历输出
print("最终学生信息：")
for k, v in student.items():
    print(k, ":", v)