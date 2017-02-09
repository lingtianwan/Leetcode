# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(candidates) == 0:
            return []
        if len(candidates) == 1:
            if candidates[0] == target:
                return [[target]]
            else:
                return []
        def dfs(cand, sum, sol_list):
            if sum == 0:
                res.append(sol_list)
            elif sum > 0:
                for i in range(len(cand)):
                    if i == 0 or cand[i] != cand[i-1]:
                        dfs(cand[i+1:], sum-cand[i], sol_list+[cand[i]])
        candidates.sort()
        dfs(candidates, target, [])
        return res
