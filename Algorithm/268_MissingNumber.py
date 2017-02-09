# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_max = len(nums)
        i = sum_max
        while i > 0:
            i -= 1
            sum_max += i
        sum_nums = 0
        for j in nums:
            sum_nums += j
        return sum_max - sum_nums
