# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        if n == 1:
            return 1
        ugly = [1]
        idx_prime = [0] * k
        m = [0] * k
        while len(ugly) < n:
            for i in range(k):
                m[i] = ugly[idx_prime[i]] * primes[i]
            min_val = min(m)
            for i in range(k):
                if min_val == m[i]:
                    idx_prime[i] += 1
            ugly.append(min_val)
        return ugly[-1]
