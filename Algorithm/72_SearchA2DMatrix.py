# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        l_row = 0
        r_row = m - 1
        while l_row < r_row - 1:
            mid = (l_row + r_row) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l_row = mid
            else:
                r_row = mid
        if matrix[l_row][0] == target or matrix[r_row][0] == target:
            return True
        if matrix[r_row][0] < target:
            row = r_row
        else:
            row = l_row
        l_col = 0
        r_col = n - 1
        while l_col < r_col - 1:
            mid = (l_col + r_col) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l_col = mid
            else:
                r_col = mid
        if matrix[row][l_col] == target or matrix[row][r_col] == target:
            return True
        return False
