# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        v_list = []
        v_idx = []
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                v_list.append(s[i])
                v_idx.append(i)
        for i in range(len(v_list)):
            s_list[v_idx[len(v_list)-1-i]] = v_list[i]
        return ''.join(s_list)
