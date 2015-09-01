__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if height == [] or len(height) == 1:
            return 0
        else:
            max_area = 0
            i, j = 0, len(height)-1
            while i < j:
                max_area = max(max_area, min(height[i], height[j])*(j-i))
                if height[i] < height[j]:
                    i += 1
                else:
                    j -= 1
            return max_area

s = Solution()
print(s.maxArea([1, 3, 1, 2]))