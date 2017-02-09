# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        a = 1
        tmp = 9
        while n > tmp:
            n -= tmp
            a += 1
            tmp = (int('9' * a) - int('9'*(a - 1))) * a
        if n % a == 0:
            return int(str(10 ** (a-1) + n / a - 1)[-1])
        num = 10 ** (a-1) + n // a
        remain = str(num)
        res = int(remain[n % a - 1])
        return res
