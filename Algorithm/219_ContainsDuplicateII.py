# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i in range(len(nums)):
            if nums[i] in lookup:
                if i - lookup[nums[i]] <= k:
                    return True
            lookup[nums[i]] = i
        return False
