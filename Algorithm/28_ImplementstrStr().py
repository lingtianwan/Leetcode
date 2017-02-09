# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)
        if m == 0:
            return 0
        if n < m:
            return -1
        startIndex = -1
        for i in range(n-m+1):
            if haystack[i] == needle[0]:
                startIndex = i
                for j in range(m):
                    if haystack[i+j] != needle[j]:
                        startIndex = -1
                        break
                if startIndex == i:
                    return i
        return -1
