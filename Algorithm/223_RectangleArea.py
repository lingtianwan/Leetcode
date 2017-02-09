# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        m = max(A, E)
        n = min(C, G)
        p = max(B, F)
        q = min(D, H)
        if n - m < 0 or q - p < 0:
            overlap = 0
        else:
            overlap = (n-m) * (q-p)
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap
