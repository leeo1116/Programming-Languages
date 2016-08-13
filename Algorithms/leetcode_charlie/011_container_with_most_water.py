__doc__ = """
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.

Note: You may not slant the container.
"""


class Solution(object):
    def __init__(self, index):
        self.index = index

    def container_with_most_water(self, height):
        """
        find the most water a container can hold
                 |
           |     |        |
        |  |  |  |     |  |
        |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |
        ---------------------------> x
        0  1  2  3  4  5  6  7
        :param height: list[int]
        :return: int
        """
        if len(height) < 2:
            return 0
        low, high = 0, len(height)-1
        max_water = (high-low)*min(height[low], height[high])
        while low < high:
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
            max_water = max(max_water, (high-low)*min(height[low], height[high]))
        return max_water

s = Solution(11)
print(s.container_with_most_water([4, 3, 2, 3]))