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
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)

        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)

        overlap = 0
        if right > left and top > bottom:
            overlap = (right-left)*(top-bottom)
        return area1+area2-overlap
