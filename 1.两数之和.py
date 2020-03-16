#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] twosum
#
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[target - nums[i]] = i
            else:
                return [temp[nums[i]], i]
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    a, b = solution.twoSum([1, 4, 5, 8, 3, 2], 7)
    print(a, b)
