# 372. Super Pow   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 10712
# Total Submissions: 32667
# Difficulty: Medium
# Contributors: Admin
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        power = a
        for i in b[::-1]:
            ans = ans * (power ** i) % 1337
            power = (power ** 10) % 1337
        return ans
