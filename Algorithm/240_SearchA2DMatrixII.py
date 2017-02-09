# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        while m > 0 and n > 0:
            if m == 1:
                return target in matrix[0]
            if n == 1:
                return [target] in matrix
            m_start = 0
            m_end = m
            n_start = 0
            n_end = n
            for i in range(m):
                if matrix[i][0] == target:
                    return True
                if matrix[i][-1] == target:
                    return True
                if matrix[i][0] < target:
                    if matrix[i][-1] < target:
                        m_start += 1
                else:
                    m_end = i
                    break
            if m_start == m_end:
                return False
            subset = matrix[m_start:m_end]
            for i in range(n):
                if subset[0][i] == target:
                    return True
                if subset[0][-1] == target:
                    return True
                if subset[0][i] < target:
                    if subset[-1][i] < target:
                        n_start += 1
                else:
                    n_end = i
                    break
            if m_start == m_end:
                return False
            matrix = [a[n_start:n_end] for a in subset]
            m = len(matrix)
            n = len(matrix[0])
        return False
