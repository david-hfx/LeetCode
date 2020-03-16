#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (33.82%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 21.9K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶:
#
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#
# #! 自己的解法，时间复杂度最好O(log(n))，最差o(n)
# class Solution:

#     def search(self, nums: List[int], target: int) -> bool:
#         if not nums:
#             return False
#         low, high = 0, len(nums) - 1
#         while low <= high:
#             mid = int((low + high) / 2)
#             if nums[mid] == target:
#                 return True
#             #! 根据各种不同的情况判断
#             if nums[mid] < nums[high]:
#                 if nums[mid] <= target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             elif nums[mid] > nums[low]:
#                 if nums[low] <= target <= nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             elif nums[mid] == nums[high] and nums[mid] != nums[low]:
#                 high = mid - 1
#             elif nums[mid] == nums[low] and nums[mid] != nums[high]:
#                 low = mid + 1
#             #! 如果首尾相等，则去重
#             else:
#                 low += 1
#         return False


#! 官方解法，稍微简洁一点
class Solution:

    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            #! 去重
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
