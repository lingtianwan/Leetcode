# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_map = {}
        for i in s:
            if i in s_map.keys():
                s_map[i] += 1
            else:
                s_map[i] = 1
        max_len = 0
        single = 0
        for i in s_map:
            if s_map[i] % 2 == 1 and single == 0:
                single = 1
            max_len += (s_map[i] // 2) * 2
        res = max_len + single
        return res
