# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = len(strs[0])
        for i in strs[1:]:
            min_len = min(min_len, len(i))
        if min_len == 0:
            return ''
        res = ''
        for i in range(min_len):
            common = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != common:
                    return res
            res += common
        return res
