# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = s[::-1]
        last = None
        res = 0
        for i in s:
            if last and nums[i] < last:
                res -= 2 * nums[i]
            res += nums[i]
            last = nums[i]
        return res
