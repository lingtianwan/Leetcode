# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        dp = [0 for i in range(n)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == len(triangle[i])-1:
                    dp[j] = dp[j-1] + triangle[i][j]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
        return min(dp)
