# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        def dfs(depth, start, val_list):
            res.append(val_list)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, val_list+[nums[i]])
        nums.sort()
        dfs(0, 0, [])
        return res
