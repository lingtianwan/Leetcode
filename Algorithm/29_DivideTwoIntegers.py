# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if abs(dividend) < abs(divisor):
            return 0
        sums = 0
        count = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            sums = b
            count = 1
            while sums + sums < a:
                sums += sums
                count += count
            a -= sums
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648
        return res
