# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dict = {}
        for i in nums:
            if i in cnt_dict:
                cnt_dict[i] += 1
            else:
                cnt_dict[i] = 1
        for j in cnt_dict:
            if cnt_dict[j] == 1:
                return j
        return
