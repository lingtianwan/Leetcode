# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == []:
            return s
        palin = ''
        for i in range(len(s)):
            len1 = len(self.getLongest(s, i, i))
            if len1 > len(palin):
                palin = self.getLongest(s, i, i)
            len2 = len(self.getLongest(s, i, i+1))
            if len2 > len(palin):
                palin = self.getLongest(s, i, i+1)
        return palin

    def getLongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
