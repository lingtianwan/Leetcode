# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.addParenthesis(n, n, '', res)
        return res

    def addParenthesis(self, l, r, item, res):
        if l > r:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.addParenthesis(l-1, r, item+'(', res)
        if r > 0:
            self.addParenthesis(l, r-1, item+')', res)
