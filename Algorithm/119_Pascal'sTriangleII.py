# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in range(2, rowIndex+1):
            temp = [1 for j in range(i+1)]
            for k in range(1, i):
                temp[k] = res[k] + res[k-1]
            res = temp[:]
            i += 1
        return res
