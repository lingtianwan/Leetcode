# Implement pow(x, n).


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)
        else:
            if n % 2:
                return self.myPow(x*x, n/2) * x
            else:
                return self.myPow(x*x, n/2)
