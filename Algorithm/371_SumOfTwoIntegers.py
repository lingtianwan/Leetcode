# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_bit = 2**32
        max_bit_compliment = -2**32
        while b != 0:
            if b == max_bit:
                return a ^ max_bit_compliment
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
