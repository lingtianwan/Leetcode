# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        digits[-1] = 0
        plus = 1
        idx = len(digits) - 2
        while plus and idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] += 1
                plus = 0
        if plus == 1:
            digits.insert(0,1)
        return digits
