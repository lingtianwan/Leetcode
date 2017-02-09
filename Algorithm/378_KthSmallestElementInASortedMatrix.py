# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) >> 1
            loc = self.lowerCount(matrix, mid)
            if loc >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def lowerCount(self, matrix, num):
        i = len(matrix) - 1
        j = 0
        cnt = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt
