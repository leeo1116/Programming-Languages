__author__ = 'liangl2'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        min_sum = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                min_sum[j] = triangle[i][j]+min(min_sum[j], min_sum[j+1])
        return min_sum[0]

s = Solution()
print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))