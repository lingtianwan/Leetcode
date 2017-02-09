# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(depth, start, val_list):
            res.append(val_list)
            if depth == len(nums):
                return
            dup = None
            for i in range(start, len(nums)):
                if nums[i] == dup:
                    continue
                dup = nums[i]
                dfs(depth+1, i+1, val_list+[nums[i]])
        nums.sort()
        dfs(0, 0, [])
        return res
