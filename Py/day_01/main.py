
from student_ms import StudentMS

if __name__ == '__main__':
    # 1. 创建学生管理系统对象
    sms = StudentMS()

    # 2. 无限循环让用户做选择，输入6则退出
    while True:
        StudentMS.print_info()
        num = input()
        if num == '1':
            sms.show()
        elif num == '2':
            sms.query()
        elif num == '3':
            sms.add()
        elif num == '4':
            sms.modify()
        elif num == '5':
            sms.delete()
        elif num == '6':
            sms.save()
            break
        else:
            print("输入的什么玩意，看清楚，重来\n")

    print("程序结束。")