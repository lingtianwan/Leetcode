# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = b = None
        for i in nums:
            if a is None or a >= i:
                a = i
            elif b is None or b >= i:
                b = i
            else:
                return True
        return False
