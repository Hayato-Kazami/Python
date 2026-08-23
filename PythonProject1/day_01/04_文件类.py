# 面向对象：一切活都让对象干
# 需求，完成文件的读写功能，既能读也能写
# 实现，以面向对象思想，搞一个对象，这个对象能读能写，让对象干活
# 1
class FileOperator:

    def __init__(self, file_path):
        # 对象被创建的时候，就打开文件了
        self.fw = open(file_path, "w", encoding="utf-8")
        self.fr = open(file_path, "r", encoding="utf-8")

    def __del__(self):
        self.fr.close()
        self.fw.close()

    def read(self):
        print(self.fr.read())

    def write(self, text):
        self.fw.write(text)
        self.fw.write("\n")
        self.fw.flush()         # 将缓冲区内容写入硬盘
# 2
fo = FileOperator("hello.txt")
# 3
fo.write("我是帅哥")
fo.read()