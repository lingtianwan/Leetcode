# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            if i == len(nums) - 1:
                res.append(nums[i])
                i += 1
            elif nums[i] == nums[i+1]:
                i += 2
            else:
                res.append(nums[i])
                i += 1
        return res
