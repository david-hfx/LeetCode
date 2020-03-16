#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.91%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 48.8K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        i = len(nums) - 1
        j = -1
        while i > 0:
            if nums[i - 1] < nums[i]:
                j = i - 1
                break
            i -= 1
        for k in range(len(nums) - 1, -1, -1):
            if nums[k] > nums[j]:
                nums[k], nums[j] = nums[j], nums[k]
                # 当字典排序不存在更大的排列时，此时j = -1，即将整个数组从小到大排序，神来之笔
                nums[j + 1:] = sorted(nums[j + 1:])
                return
