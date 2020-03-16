#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (65.57%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 34.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
from typing import List


# 回溯算法,better
class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        # 如果目标值小于0，则返回（回溯）
        if target < 0:
            return
        # 完美值，加入
        if target == 0:
            res.append(path)
            return
        # 循环迭代，如果满足条件，则返回，否则回溯
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


# 另一种解法,也是回溯算法，但是worse
class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(i, temp_sum, temp):
            if temp_sum > target:
                return
            if temp_sum == target:
                res.append(temp)
                return
            for j in range(i, n):
                backtrack(j, temp_sum + candidates[j], temp + [candidates[j]])

        backtrack(0, 0, [])
        return res
