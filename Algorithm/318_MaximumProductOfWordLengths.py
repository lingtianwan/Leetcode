# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        if n == 0:
            return 0
        elements = [0] * n
        for i in range(n):
            for c in words[i]:
                elements[i] |= 1 << (ord(c)-ord('a'))
        max_val = 0
        for i in range(n):
            for j in range(1,n):
                if elements[i] & elements[j] == 0:
                    max_val = max(max_val, len(words[i])*len(words[j]))
        return max_val
