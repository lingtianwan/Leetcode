# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) == 0 or len(t) == 0:
            return False
        match = {}
        for i in range(len(s)):
            a = s[i]
            c = t[i]
            if a not in match and c not in match.values():
                match[a] = c
            elif a in match:
                if match[a] != c:
                    return False
            else:
                return False
        return True
