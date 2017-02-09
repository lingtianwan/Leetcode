# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        dp = [0] * n
        pre = [None] * n
        for x in range(n):
            for y in range(x):
                if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
                    dp[x] = dp[y] + 1
                    pre[x] = y
        idx = dp.index(max(dp))
        ans = []
        while idx is not None:
            ans.append(nums[idx])
            idx = pre[idx]
        return ans
