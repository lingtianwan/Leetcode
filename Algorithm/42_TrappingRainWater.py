# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax = 0
        rightmax = 0
        total = 0
        left_high = [0 for i in range(len(height))]
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            left_high[i] = leftmax
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(left_high[i], rightmax) > height[i]:
                total += min(left_high[i], rightmax) - height[i]
        return total
