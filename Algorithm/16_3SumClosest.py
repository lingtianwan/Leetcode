# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == target:
                    return target
                if ans is None or abs(sums - target) < abs(ans - target):
                    ans = sums
                if sums < target:
                    left += 1
                else:
                    right -= 1
        return ans
