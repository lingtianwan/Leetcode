# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        missing = n
        lt = {}
        for i in t:
            if i in lt:
                lt[i] += 1
            else:
                lt[i] = 1
        i = 0
        I = 0
        J = 0
        for j, c in enumerate(s, 1):
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1
            while i < j and missing == 0:
                if J == 0 or j - i < J - I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]
