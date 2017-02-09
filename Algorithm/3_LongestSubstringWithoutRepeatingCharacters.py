# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_uniq = []
        max_val = 0
        for i in s:
            if i in s_uniq:
                del s_uniq[0:s_uniq.index(i)+1]
            s_uniq.append(i)
            max_val = max(max_val, len(s_uniq))
        return max_val
