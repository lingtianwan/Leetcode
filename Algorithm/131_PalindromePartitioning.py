# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        if len(s) == 0:
            return []
        self.dfs(s, [])
        return Solution.res

    def isPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return True
        for i in range(n / 2):
            if s[i] != s[n-1-i]:
                return False
        return True

    def dfs(self, s, string_list):
        if len(s) == 0:
            Solution.res.append(string_list)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], string_list + [s[:i]])
        return
