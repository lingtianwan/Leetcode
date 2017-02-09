# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
#
# Hint:
#
# How many majority elements could it possibly have?
# Do you have a better hint? Suggest it!


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = None
        n2 = None
        c1 = 0
        c2 = 0
        for i in nums:
            if i == n1:
                c1 += 1
            elif i == n2:
                c2 += 1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 == 0:
                n2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        return [ n for n in (n1, n2) if n is not None and nums.count(n) > len(nums) / 3]
