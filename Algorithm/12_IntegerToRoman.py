# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        m = num // 1000
        num = num % 1000
        res += 'M' * int(m)
        d = num // 500
        num = num % 500
        c = num // 100
        num = num % 100
        if c == 4:
            res += 'C'
            if d > 0:
                res += 'M'
            else:
                res += 'D'
        else:
            res += 'D' * int(d)
            res += 'C' * int(c)
        l = num // 50
        num = num % 50
        x = num // 10
        num = num % 10
        if x == 4:
            res += 'X'
            if l > 0:
                res += 'C'
            else:
                res += 'L'
        else:
            res += 'L' * int(l)
            res += 'X' * int(x)
        v = num // 5
        num = num % 5
        if num == 4:
            res += 'I'
            if v > 0:
                res += 'X'
            else:
                res += 'V'
        else:
            res += 'V' * int(v)
            res += 'I' * num
        return res
