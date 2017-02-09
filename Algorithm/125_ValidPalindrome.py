# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        n = len(s)
        start = 0
        end = n - 1
        while start < end:
            while (not (s[start].isalpha() or s[start].isnumeric())) and start < end:
                start += 1
            while (not (s[end].isalpha() or s[end].isnumeric())) and start < end:
                end -= 1
            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
