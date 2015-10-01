__author__ = 'Liang Li'
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_vol = 0
        max_left, max_right = 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    max_vol += max_left-height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    max_vol += max_right-height[right]
                right -= 1
        return max_vol

s = Solution()
print(s.trap([0, 2, 0]))