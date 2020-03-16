#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (35.63%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 43.3K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
#
#
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
#
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
#
#

from typing import List


# if i not in nums算法时间复杂度好像超了。。。
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


# 官方解法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1

        if n == 1:
            return 2

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 使用索引和数字符号作为检查器
        # 例如nums[1]为负数，代表1在里面出现过
        # nums[2]为整数，代表2在里面没出现过
        for i in range(n):
            a = abs(nums[i])

            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        # 先看1~n-1中有没有正的
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # 如果前n-1个数中没有正的，那就检查第n个数的
        if nums[0] > 0:
            return n

        # 如果前n个数都为负，则返回n+1
        return n + 1
