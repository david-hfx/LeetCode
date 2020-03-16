#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
#!自己写的
# class Solution:

#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if not nums:
#             return None
#         counts = {'0': 0, '1': 0, '2': 0}
#         for num in nums:
#             if num == 0:
#                 counts['0'] += 1
#             elif num == 1:
#                 counts['1'] += 1
#             else:
#                 counts['2'] += 1
#         nums[:] = [0] * counts['0'] + [1] * counts['1'] + [2] * counts['2']


#? 标准答案,三指针法
class Solution:

def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
