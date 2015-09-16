__author__ = 'liangl2'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        min_sum = triangle[0][0]
        pre_index = 0
        for i in range(1, len(triangle)):
            if triangle[i][pre_index] < triangle[i][pre_index+1]:
                min_sum += triangle[i][pre_index]
                pre_index = pre_index
            else:
                min_sum += triangle[i][pre_index+1]
                pre_index += 1
        return min_sum

s = Solution()
print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))