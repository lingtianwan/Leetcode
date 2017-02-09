# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, count, string):
            if count == 4 and len(s) == 0:
                res.append(string[:-1])
            if count == 4:
                return
            if len(s) == 0:
                return
            for i in range(1,4):
                if i <= len(s) and int(s[:i]) <= 255 and ((i == 1) or (s[0] != '0' and i > 1)):
                    dfs(s[i:], count+1, string+s[:i]+'.')
        res = []
        if len(s) <= 3:
            return []
        dfs(s, 0, '')
        return res
