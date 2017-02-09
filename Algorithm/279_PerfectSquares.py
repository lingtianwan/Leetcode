# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        a = 0
        while a * a <= n:
            b = int(math.sqrt(n - a * a))
            if a * a + b * b == n:
                if a == 0:
                    return 1
                else:
                    return 2
            a += 1
        return 3
