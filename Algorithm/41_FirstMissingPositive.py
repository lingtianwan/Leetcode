# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        for i in range(n):
            while nums[i] > 0 and nums[i] - 1 != i:
                if nums[i] - 1 < n and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    nums[i] = 0
        for i in range(n):
            if nums[i] <= 0:
                return i + 1
        return n + 1
