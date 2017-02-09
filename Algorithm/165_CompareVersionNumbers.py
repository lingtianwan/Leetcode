# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if len(version1) == 0 and len(version2) == 0:
            return 0
        tmp1 = '0'
        tmp2 = '0'
        pos1 = 0
        pos2 = 0
        for i in range(len(version1)):
            pos1 += 1
            if version1[i] == '.':
                break
            tmp1 += version1[i]
        for i in range(len(version2)):
            pos2 += 1
            if version2[i] == '.':
                break
            tmp2 += version2[i]
        if int(tmp1) > int(tmp2):
            return 1
        elif int(tmp1) < int(tmp2):
            return -1
        else:
            return self.compareVersion(version1[pos1:], version2[pos2:])
