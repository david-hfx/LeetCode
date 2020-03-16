#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (35.44%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 58.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
#
#
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#
#
# from typing import List
# import pysnooper


# class Solution:
#     # @pysnooper.snoop()
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True

#         if nums[0] == 0 and len(nums) > 1:
#             return False

#         for index, num in enumerate(nums):
#             if num == 0 and index == len(nums) - 1:
#                 for i in range(index - 1, -1, -1):
#                     if nums[i] + i >= index:
#                         return True
#             if num == 0 and index != len(nums) - 1:
#                 for i in range(index - 1, -1, -1):
#                     if nums[i] + i > index:
#                         break
#                     elif i == 0:
#                         return False
#         return True


# 简单的方法
class Solution:
    def canJump(self, nums):
        m = 0
        for index, num in enumerate(nums):
            if index > m:
                return False
            m = max(m, index + num)
        return True
