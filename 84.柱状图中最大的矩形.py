#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (38.21%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 21.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#
from typing import List


# import pysnooper
class Solution:
    # @pysnooper.snoop()
    """[summary]
    利用栈的思想,初始化栈为-1，表示开始，初始化时，按照从左到右的顺序，将柱子序号不断放进栈中
    直到相邻的柱子呈下降关系，即height[i-1] > height[i]时，弹出栈中的序号，直到height[stack[j]] <= a[i]，每次弹出下标时，用弹出元素作为高当前元素到stack[top-1]之间的距离为宽作为最大面积。
    """

    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


# # !暴力求解法，时间复杂度为o(n^2)，超出时间限制，无法AC
# class Solution:
#     # @pysnooper.snoop()
#     def largestRectangleArea(self, height):
#         maxarea = 0
#         for i in range(len(height)):
#             minheight = float('inf')
#             for j in range(i, len(height)):
#                 minheight = min(minheight, height[j])
#                 maxarea = max(maxarea, minheight * (j - i + 1))
#         return maxarea

# #! DP分治法，先找到最低的柱子，然后计算以最低柱子为高的面积，然后计算左右两边，左右两边也去找最低柱子,时间复杂度o(nlog(n))，当柱子为排序时，时间复杂度为o(n^2)，无任何优化效果，无法AC
# class Solution:

#     def largestRectangleArea(self, height):
#         start, end = 0, len(height) - 1
#         return self.dp(height, start, end)

#     def dp(self, height, start, end):
#         if start > end:
#             return 0
#         minindex = start
#         for i in range(start, end + 1):
#             if height[minindex] > height[i]:
#                 minindex = i
#         return max(
#             height[minindex] * (end - start + 1),
#             max(
#                 self.dp(height, start, minindex - 1),
#                 self.dp(height, minindex + 1, end)))

# a = largestRectangleArea([2, 1, 5, 6, 2, 3])
