"""
给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。

输入描述

第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，
表示数组的元素。随后的输入为需要计算总和的区间，直至文件结束。

输出描述

输出每个指定区间内元素的总和。

输入示例
5
1
2
3
4
5
0 1
1 3

输出示例
3
9

"""

from typing import List
import random

class Solution:
    def creat_list(self):
        nums = int(input("请输入数组长度:"))
        lst = [random.randint(0, 100) for _ in range(nums)]
        print(nums)
        for i in lst:
            print(i, end="\n")
        return lst

    def creat_list1(self):
        nums = int(input("请输入数组长度:"))
        lst1 = []
        for i in range(nums):
            x = int(input(f"请输入第{i+1}个元素:"))
            lst1.append(x)
        return lst1

    def add(self, lst: List[int]):
        # ① 建一次前缀和表（放在 while True 外面）
        pre = [0] * (len(lst) + 1)
        for i in range(len(lst)):
            pre[i + 1] = pre[i] + lst[i]

        while True:
            s = input("请输入区间（如 0 1，输入 q 退出）：")
            if s.strip().lower() == "q":
                break
            low, high = map(int, s.split())
            total = pre[high + 1] - pre[low]
            print(f"{low} {high}")
            print(total)



if __name__ == "__main__":
    
    Solution().add(Solution().creat_list())