#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (44.52%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 11.2K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
#
#
class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """与矩形面积那题思路类似，在外面套上一个变成矩形面积题的框
        
        Arguments:
            matrix {List[List[str]]} -- 给定一个只有'1'和'0'的字符串矩阵
        
        Returns:
            int -- 返回矩阵中'1'围成的矩形的最大面积
        """
        if not matrix or not matrix[0]:
            return 0
        r = len(matrix[0])
        height = [0] * (r + 1)
        ans = 0
        for row in matrix:
            for j in range(r):
                #! 如果上下的1是连续的就加1，如果上面是1，如果下面是0，则置0
                height[j] = height[j] + 1 if row[j] == '1' else 0
            stack = [-1]
            for k in range(r + 1):
                while height[stack[-1]] > height[k]:
                    h = height[stack.pop()]
                    w = k - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(k)
        return ans
