# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        new_nums = sorted([str(x) for x in nums], cmp=self.compare)
        if new_nums[0] == '0':
            return '0'
        else:
            return ''.join(new_nums)

    def compare(self, a, b):
        if a + b > b + a:
            return -1
        else:
            return 1
