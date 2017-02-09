# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(candidates) == 0:
            return []
        def dfs(cand, sum, sol_list):
            if sum == 0:
                res.append(sol_list)
            elif sum > 0:
                for i in range(len(cand)):
                    dfs(cand[i:], sum-cand[i], sol_list+[cand[i]])
        candidates.sort()
        dfs(candidates, target, [])
        return res
