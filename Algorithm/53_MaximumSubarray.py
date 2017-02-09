# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        min_sum = 0
        total = 0
        for i in nums:
            total += i
            if total - min_sum > max_sum:
                max_sum = total - min_sum
            if total < min_sum:
                min_sum = total
        return max_sum
