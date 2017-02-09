# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word in anagram_map:
                anagram_map[sort_word].append(word)
            else:
                anagram_map[sort_word] = [word]
        res = []
        for key, value in anagram_map.items():
            res.append(value)
        return res
