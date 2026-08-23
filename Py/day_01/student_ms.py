from student import Student


class StudentMS(object):
    """
    学生管理系统类。

    主要负责：
    1. 程序启动时，从文件中读取学生信息；
    2. 在内存中用字典保存学生对象；
    3. 提供查询、添加、修改、删除、保存等操作。
    """

    # 类属性：记录学生信息的文件路径。
    # 这个路径被所有 StudentMS 对象共享。
    # 当前使用相对路径 "stu.json"，表示从程序运行时所在目录查找该文件。
    stu_file_path = "stu.json"

    def __init__(self):
        # 实例属性：保存所有学生信息的字典。
        # 字典结构：
        # {
        #     "学生姓名": 学生类对象,
        #     "学生姓名": 学生类对象,
        #     ...
        # }
        # 这样设计后，可以通过学生姓名快速找到对应的 Student 对象。
        self.stu_dict = {}

        try:
            # 打开保存学生信息的文件。
            # "r" 表示只读模式。
            # encoding="utf-8" 用于正确读取中文内容。
            f = open(StudentMS.stu_file_path, "r", encoding="utf-8")

            # 一次性读取文件中的所有行。
            # 当前设计中，文件的每一行都是一个 JSON 字符串，
            # 每个 JSON 字符串对应一个学生对象。
            lines: list = f.readlines()

            # 读取完成后关闭文件，释放资源。
            f.close()

            # 遍历文件中的每一行学生数据。
            for line in lines:
                # 去掉字符串前后的空格、换行符和回车符。
                # 例如：'{"name": "张三"}\n' -> '{"name": "张三"}'
                line = line.strip()

                # 把 JSON 字符串转换成 Student 对象。
                # Student.generate 是 student.py 中定义的静态方法。
                stu = Student.generate(line)

                # 将学生对象添加到字典中。
                # key 使用学生姓名，value 使用学生对象。
                # 如果添加了同名学生，后面的数据会覆盖前面的数据。
                self.stu_dict[stu.name] = stu
        except FileNotFoundError as e:
            # 如果文件不存在，说明系统可能是第一次运行。
            # 这里没有直接报错退出，而是打印提示，让程序继续运行。
            print(f"记录学生信息的文件{StudentMS.stu_file_path}不存在，系统第一次运行")

    def save(self):
        """
        保存学生信息到文件。

        把当前内存中的 self.stu_dict 写回 stu.json。
        每个学生对象写成一行 JSON 字符串。
        """
        # 以写入模式打开文件。
        # "w" 会清空原文件内容，再写入新的内容。
        f = open(StudentMS.stu_file_path, "w", encoding="utf-8")

        # 遍历学生字典中的所有 Student 对象。
        for stu in self.stu_dict.values():
            # print(stu) 会自动调用 str(stu)。
            # 但是 f.write() 只能写字符串，所以这里需要手动使用 str(stu)。
            # Student 类中定义了 __str__ 方法，因此 str(stu) 会得到 JSON 字符串。
            f.write(str(stu))

            # 每个学生写完后换行，保证一个学生占文件中的一行。
            f.write("\n")

        # 写入完成后关闭文件。
        f.close()

    def show(self):
        """
        显示全部学生信息。

        :return: None
        """
        # 如果学生字典为空，说明当前没有任何学生信息。
        if len(self.stu_dict) == 0:
            print("【查询全部学生】暂无学生")
            return

        # 字典不为空时，逐个打印学生信息。
        print("【查询全部学生】")
        for stu in self.stu_dict.values():
            print(f"姓名：{stu.name}, 性别：{stu.gender}, 手机：{stu.tel}，年龄：{stu.age}，外号：{stu.nickname}")

    def query(self):
        """
        根据姓名查询单个学生信息。

        用户输入姓名后，程序会到 self.stu_dict 中查找对应学生。
        """
        # 获取用户要查询的学生姓名。
        name = input("【查询学生】请输入要查询的学生姓名：")

        # 判断字典中是否存在这个学生姓名。
        if name not in self.stu_dict:
            print(f"【查询学生】没有{name}这个学生")
            return

        # 根据姓名取出对应的 Student 对象，并打印详细信息。
        stu = self.stu_dict[name]
        print(f"查到学生，姓名：{stu.name}, 性别：{stu.gender}, 手机：{stu.tel}，年龄：{stu.age}，外号：{stu.nickname}")

    def add(self):
        """
        添加一个新的学生信息。

        通过 input 获取学生的各项信息，创建 Student 对象后保存到字典中。
        """
        # 逐项接收用户输入的学生信息。
        name = input("【添加学生】请输入学生的姓名")
        gender = input("【添加学生】请输入学生的性别")
        tel = input("【添加学生】请输入学生的手机")
        age = input("【添加学生】请输入学生的年龄")
        nickname = input("【添加学生】请输入学生的外号")

        # 根据输入内容创建 Student 对象。
        stu = Student(name, gender, tel, age, nickname)

        # 把新学生保存到字典中。
        # key 是学生姓名，value 是 Student 对象。
        self.stu_dict[name] = stu

    def modify(self):
        """
        修改已有学生信息。

        先根据姓名判断学生是否存在。
        存在则重新输入信息，并用新的 Student 对象覆盖旧对象。
        """
        # 获取要修改的学生姓名。
        name = input("【修改学生】请输入要修改学生的姓名")

        # 修改前先判断学生是否存在。
        if name not in self.stu_dict:
            print(f"【修改学生】没有{name}这个学生")
            return

        # 学生存在时，重新输入该学生的信息。
        gender = input("【修改学生】请输入学生的性别")
        tel = input("【修改学生】请输入学生的手机")
        age = input("【修改学生】请输入学生的年龄")
        nickname = input("【修改学生】请输入学生的外号")

        # 创建新的 Student 对象。
        stu = Student(name, gender, tel, age, nickname)

        # 因为 name 已经存在，所以这里会覆盖原来的学生对象。
        self.stu_dict[name] = stu

    def delete(self):
        """
        删除指定学生信息。

        根据用户输入的姓名，从 self.stu_dict 中删除对应学生。
        """
        # 获取要删除的学生姓名。
        name = input("【删除学生】请输入要删除的学生姓名")

        # 如果学生不存在，就不需要删除。
        if name not in self.stu_dict:
            print(f"【删除学生】学生{name}不存在，无需删除")
            return

        # pop 根据 key 删除字典中的数据。
        self.stu_dict.pop(name)
        print(f"【删除学生】{name}删除成功")

    @staticmethod
    def print_info():
        """
        打印系统功能菜单。

        这个方法不需要访问实例属性或类属性，
        所以定义成静态方法。
        """
        print("\n欢迎来到黑马学生管理系统V1.0版，请输入你选择的功能")
        print("1. 查询全部学生信息")
        print("2. 查询单个学生信息")
        print("3. 添加一个学生信息")
        print("4. 修改一个学生信息")
        print("5. 删除一个学生信息")
        print("6. 退出程序")
        print("请输入你的选择：")
        print("-"*10)
        print("\n")


# 只有直接运行当前文件时，下面的代码才会执行。
# 如果当前文件被其他文件 import，这部分代码不会执行。
if __name__ == '__main__':
    # 创建学生管理系统对象。
    # 创建对象时会自动读取 stu.json，并把文件内容加载到 stu_dict 中。
    sms = StudentMS()

    # 调试代码：可以直接查看字典结构。
    # print(sms.stu_dict)

    # 调试代码：可以手动保存当前学生数据。
    # sms.save()

    # 先显示当前已有学生。
    sms.show()

    # 添加一个新学生。
    sms.add()

    # 再次显示学生列表，观察添加后的结果。
    sms.show()
