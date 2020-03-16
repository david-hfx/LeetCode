#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        r, c = len(matrix), len(matrix[0])
        rs, re = 0, r - 1
        while rs <= re:
            rmid = int((rs + re) / 2)
            if matrix[rmid][0] > target:
                re -= 1
            elif matrix[rmid][0] < target:
                rs += 1
            else:
                return True
        cs, ce = 0, c - 1
        while cs <= ce:
            cmid = int((cs + ce) / 2)
            if matrix[re][cmid] > target:
                ce -= 1
            elif matrix[re][cmid] < target:
                cs += 1
            else:
                return True
        return False
