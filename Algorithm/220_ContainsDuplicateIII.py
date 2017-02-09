# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        l = sorted(zip(nums, range(n)), key=lambda x:x[0])
        po = 0
        while po < n:
            i = po + 1
            while i < len(l):
                if abs(l[i][0] - l[po][0]) <= t and abs(l[i][1] - l[po][1]) <= k:
                    return True
                else:
                    if abs(l[i][0] - l[po][0]) > t:
                        break
                    else:
                        i += 1
            po += 1
        return False
