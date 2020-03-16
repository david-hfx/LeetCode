#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (34.34%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 17.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#
# class Solution:
#     def insert(self, intervals: List[List[int]],
#                newInterval: List[int]) -> List[List[int]]:
#         intervals = intervals + [newInterval]
#         intervals.sort(key=lambda x: x[0])
#         out = []
#         for i in intervals:
#             if out and i[0] <= out[-1][-1]:
#                 out[-1][-1] = max(out[-1][-1], i[-1])
#             else:
#                 out += [i]
#         return out


class Solution:
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[-1]
        left = [i for i in intervals if i[-1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][-1])
        return left + [[s, e]] + right
