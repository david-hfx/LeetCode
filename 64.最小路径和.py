#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (61.52%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 31K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#
# !第一次跟标准答案一样，奖励自己一下
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, c):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
