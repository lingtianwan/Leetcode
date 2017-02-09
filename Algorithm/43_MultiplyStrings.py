# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note:
# The numbers can be arbitrarily large and are non-negative.
# Converting the input string to integer is NOT allowed.
# You should NOT use internal library such as BigInteger.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp[i + j] += int(num1[i]) * int(num2[j])
        res = []
        for i in range(len(temp)):
            digit = temp[i] % 10
            carry = temp[i] // 10
            if i + 1 < len(temp):
                temp[i + 1] += carry
            res.insert(0, str(digit))
        res.insert(0, str(carry))
        while res[0] == "0" and len(res) > 1:
            del res[0]
        return ''.join(res)
