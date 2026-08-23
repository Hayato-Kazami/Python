"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
# 1. 暴力破解
"""
外层 i 固定子数组起点，内层 j 从 i 向右扩展。
total 累积 nums[i..j] 的和，一旦 ≥ target 就更新 result 并 break
（因为 j 再往后走只会更长，不是最短）。遍历完所有起点，
result 里就是最短长度；如果还是无穷大，说明不存在，返回 0。
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = float('inf')

        for i in range(n):          # 子数组起点
            total = 0
            for j in range(i, n):   # 子数组终点
                total += nums[j]    # 累加 nums[i..j] 的和
                if total >= target:
                    result = min(result, j - i + 1)
                    break           # 起点 i 已找到最短，无需继续往右加
        return result if result != float('inf') else 0
    

# 2. 滑动窗口
"""
思路：用左右两个指针维护一个窗口，right 不断向右累加；
一旦窗口内和 ≥ target，就记录当前长度，并收缩 left 看能不能更短。
两个指针各走一遍，时间复杂度 O(n)。
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        result = float('inf')   # 先设成无穷大

        for right in range(len(nums)):
            total += nums[right]            # 右指针扩张，累加和
            while total >= target:          # 窗口和达标，尝试收缩左边界
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return result if result != float('inf') else 0