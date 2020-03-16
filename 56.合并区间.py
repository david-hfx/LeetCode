#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.68%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 49.3K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         n = len(intervals)

#         if n <= 1:
#             return intervals

#         intervals.sort(key=lambda x: x[0])
#         i = 0
#         while i < n - 1:
#             if intervals[i][-1] < intervals[i + 1][0]:
#                 i += 1
#                 continue

#             if intervals[i + 1][0] <= intervals[i][-1] <= intervals[i + 1][-1]:
#                 intervals[i] = [intervals[i][0], intervals[i + 1][-1]]
#                 intervals.pop(i + 1)
#                 n -= 1
#                 continue

#             if intervals[i][-1] >= intervals[i + 1][-1]:
#                 intervals.pop(i + 1)
#                 n -= 1
#                 continue

#         return intervals


class Solution:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out += [i]
        return list(out)
