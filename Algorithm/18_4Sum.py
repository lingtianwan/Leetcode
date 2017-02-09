# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        res = set()
        sum_dict = {}
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] not in sum_dict:
                    sum_dict[nums[i]+nums[j]] = [(i, j)]
                else:
                    sum_dict[nums[i]+nums[j]].append((i, j))
        for i in range(n):
            for j in range(i+1, n-2):
                key = target - (nums[i] + nums[j])
                if key in sum_dict:
                    for value in sum_dict[key]:
                        if value[0] > j:
                            res.add((nums[i], nums[j], nums[value[0]], nums[value[1]]))
        return [list(i) for i in res]
