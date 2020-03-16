#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (73.28%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 15.4K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
# from typing import List
# import pysnooper


class Solution:
    # @pysnooper.snoop()
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            # list(map(list, zip(*[[]]))) == []
            A = [list(range(lo, hi))] + list(map(list, zip(*A[::-1])))
        return A
