# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
#
# Hint:
#
# Expected runtime complexity is in O(log n) and the input is sorted.


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        left = 0
        right = n - 1
        max_h = 0
        while left <= right:
            mid = (left + right) / 2
            paper = n - mid
            if citations[mid] >= paper:
                max_h = max(max_h, paper)
                right = mid - 1
            else:
                left = mid + 1
        return max_h
