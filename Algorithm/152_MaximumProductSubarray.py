# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        min_tmp = nums[0]
        max_tmp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            a = nums[i] * max_tmp
            b = nums[i] * min_tmp
            c = nums[i]
            max_tmp = max(max(a, b), c)
            min_tmp = min(min(a, b), c)
            if max_tmp > result:
                result = max_tmp
        return result
