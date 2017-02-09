# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        queue = [(beginWord, 1)]
        while queue:
            cur = queue.pop(0)
            word = cur[0]
            length = cur[1]
            if word == endWord:
                return length
            for i in range(len(beginWord)):
                part1 = word[:i]
                part2 = word[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != word[i]:
                        new_word = part1 + j + part2
                        if new_word in wordList:
                            queue.append((new_word, length+1))
                            wordList.remove(new_word)
        return 0
