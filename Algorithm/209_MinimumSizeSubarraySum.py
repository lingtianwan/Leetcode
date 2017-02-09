# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        sum = 0
        size = len(nums)
        ans = size + 1
        while right < size:
            while sum < s and right < size:
                sum += nums[right]
                right += 1
            while sum >= s and left < right:
                sum -= nums[left]
                ans = min(ans, right - left)
                left += 1
        if ans <= size:
            return ans
        else:
            return 0
