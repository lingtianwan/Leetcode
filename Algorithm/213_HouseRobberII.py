# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp1 = [0, nums[0]]
        dp2 = [0, nums[1]]
        for i in range(1, len(nums)-1):
            dp1.append(max(nums[i] + dp1[i-1], dp1[i]))
            dp2.append(max(nums[i+1] + dp2[i-1], dp2[i]))
        return max(dp1[-1], dp2[-1])
