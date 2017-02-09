# 96. Unique Binary Search Trees  QuestionEditorial Solution  My Submissions
# Total Accepted: 98603
# Total Submissions: 252198
# Difficulty: Medium
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
