# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        res = [[0 for i in range(n)] for j in range(n)]
        top = n
        right = n-1
        bottom = n-1
        left = n-2
        direction = "top"
        i = 0
        j = 0
        for k in range(1,n ** 2 + 1):
            print(str(i) + " " + str(j))
            res[i][j] = k
            print("k= " + str(k))
            if direction == "top":
                if j + 1 == top:
                    direction = "right"
                    i += 1
                    top -= 1
                else:
                    j += 1
            elif direction == "right":
                if i == right:
                    direction = "bottom"
                    j -= 1
                    right -= 1
                else:
                    i += 1
            elif direction == "bottom":
                if n - j - 1 == bottom:
                    direction = "left"
                    i -= 1
                    bottom -= 1
                else:
                    j -= 1
            elif direction == "left":
                if n - i - 1 == left:
                    direction = "top"
                    j += 1
                    left -= 1
                else:
                    i -= 1
        return res
