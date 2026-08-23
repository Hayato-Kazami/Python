import sys
from typing import List

class Solution:
    def creat_list(self):
        data = sys.stdin.read().split()
        nums = int(data[0])
        lst = [int(data[i]) for i in range(1, nums + 1)]
        self.data = data
        self.idx = nums + 1
        return lst

    def add(self, lst: List[int]):
        pre = [0] * (len(lst) + 1)
        for i in range(len(lst)):
            pre[i + 1] = pre[i] + lst[i]

        out = []
        idx = self.idx
        while idx + 1 < len(self.data):
            low = int(self.data[idx])
            high = int(self.data[idx + 1])
            out.append(str(pre[high + 1] - pre[low]))
            idx += 2
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    Solution().add(Solution().creat_list())