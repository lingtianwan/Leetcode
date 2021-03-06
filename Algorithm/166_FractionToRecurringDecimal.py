# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Hint:
#
# No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
# Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
# Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if numerator * denominator < 0:
            sign = -1
        num = abs(numerator)
        den = abs(denominator)
        remain = {}
        cnt = 0
        num_list = []
        repeat_str = None
        while True:
            num_list.append(str(num / den))
            cnt += 1
            num = 10 * (num % den)
            if num == 0:
                break
            loc = remain.get(num)
            if loc:
                repeat_str = ''.join(num_list[loc:cnt])
                break
            remain[num] = cnt
        res = num_list[0]
        if len(num_list) > 1:
            res += '.'
        if repeat_str:
            res += ''.join(num_list[1:len(num_list)-len(repeat_str)]) + '(' + repeat_str + ')'
        else:
            res += ''.join(num_list[1:])
        if sign == -1:
            res = '-' + res
        return res
