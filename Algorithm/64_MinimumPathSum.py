# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j > 0:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[m-1][n-1]
