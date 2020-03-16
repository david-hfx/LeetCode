#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (53.65%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 25.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# 输出:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# 示例 2:
#
# 输入:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# 输出:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
# 进阶:
#
#
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
#
#
#
# !自己写的，空间复杂度为O(mxn)
# class Solution:

#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         r, c = len(matrix), len(matrix[0])
#         m = []
#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j] == 0:
#                     m.append([i, j])

#         for i, j in m:
#             for k in range(r):
#                 matrix[k][j] = 0
#             for l in range(c):
#                 matrix[i][l] = 0


#! 优化后的程序，空间复杂度为o(1)
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        for i in range(1, r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, r):
            for j in range(c - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowHasZero:
            matrix[0] = [0] * c
