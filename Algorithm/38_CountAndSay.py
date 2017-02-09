# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ''
        if n == 1:
            return '1'
        x = '1'
        for i in range(n-1):
            y = ''
            next = ''
            count = 0
            for j in x:
                if next == '':
                    next = j
                    count += 1
                elif next == j:
                    count += 1
                else:
                    y += str(count)
                    y += next
                    next = j
                    count = 1
            y += str(count)
            y += next
            x = y
            i += 1
        return x
