#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (36.83%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 59.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def searchleft(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = int((low + high) / 2)
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def searchright(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = int((low + high) / 2)
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        low, high = searchleft(nums, target), searchright(nums, target)

        return [low, high] if low <= high else [-1, -1]
