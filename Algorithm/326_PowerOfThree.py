# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** round(math.log(n,3)) == n
