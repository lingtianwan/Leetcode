# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = 0
        num_b = 0
        for i in range(len(a)):
            if a[-1-i] == '1':
                num_a += 2 ** i
        for i in range(len(b)):
            if b[-1-i] == '1':
                num_b += 2 ** i
        total = num_a + num_b
        return bin(total)[2:]
