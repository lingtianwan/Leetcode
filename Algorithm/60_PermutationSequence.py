# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for i in range(n):
            fac.append(fac[-1] * (i+1))
        res = []
        elegible = range(1, n+1)
        for i in range(n):
            digit = (k - 1) // fac[n - i - 1]
            res.append(elegible[digit])
            del elegible[digit]
            k = (k - 1) % fac[n - i - 1] + 1
        return "".join(str(x) for x in res)
