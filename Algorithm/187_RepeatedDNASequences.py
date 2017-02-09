# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        lookup = {}
        res = []
        for i in range(len(s) - 9):
            if s[i:i+10] in lookup:
                lookup[s[i:i+10]] += 1
            else:
                lookup[s[i:i+10]] = 1
        for i in lookup:
            if lookup[i] > 1:
                res.append(i)
        return res
