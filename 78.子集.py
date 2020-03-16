#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#! 迭代计算
from typing import List

# class Solution:

#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return [nums]
#         res = [[]]
#         for num in sorted(nums):
#             res += [item + [num] for item in res]
#         return res
#! 递归
# class Solution:

#     def subsets(self, nums):
#         res = []
#         self.dfs(sorted(nums), 0, [], res)
#         return res

#     def dfs(self, nums, index, path, res):
#         res.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, i + 1, path + [nums[i]], res)


#! 位运算
class Solution:

    def subsets(self, nums):
        res = []
        nums.sort()
        #? 1<<len(nums) 相当于1*2^len(nums)
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j) == 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
