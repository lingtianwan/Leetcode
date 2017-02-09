# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []
        left = 0
        up = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if (up > down) or (left > right):
                return res
            direction = (direction + 1) % 4
