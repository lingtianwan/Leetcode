# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        prev_num = None
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == prev_num:
                continue
            prev_num = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
