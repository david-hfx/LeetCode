#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (54.49%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 46.8K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
#
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#
#
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28
#
#
# from typing import List
# import pysnooper

# ? !解法一，递归，但是会溢出
# class Solution:
# @pysnooper.snoop()
# def uniquePaths(m: int, n: int) -> int:
#     if m == 1 or n == 1:
#         return 1
#     else:
#         return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

# !解法二，直接通项公式
# import math

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return int(
#             math.factorial(m + n - 2) / math.factorial(m - 1) /
#             math.factorial(n - 1))

# !解法三，利用递推公式，前面的结果都保存下来，空间复杂度O(mxn)，时间复杂度O(mxn)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         a = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

#         for i in range(1, m):
#             for j in range(1, n):
#                 a[i][j] = a[i - 1][j] + a[i][j - 1]

#         return a[-1][-1]

解法四，对解法三优化，降低空间复杂度为O(n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                ans[j] += ans[j - 1]
        return ans[-1]

# !调试
# import pysnooper


# @pysnooper.snoop()
# def uniquePaths(m, n):
#     ans = [1] * n
#     for i in range(1, m):
#         for j in range(1, n):
#             ans[j] += ans[j - 1]
#     return ans[-1]


# a = uniquePaths(4, 3)
