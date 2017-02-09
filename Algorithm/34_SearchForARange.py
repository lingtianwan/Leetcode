# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
        else:
            return res
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            res[1] = right
        elif nums[left] == target:
            res[1] = left
        else:
            return res
        return res
