__author__ = 'Liang Li'
from fractions import gcd
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        points_dict = {}

        i = 0
        while i < len(points):
            dup_count = 1
            for j in range(i+1, len(points)):
                a = points[j].y-points[i].y
                b = points[i].x-points[j].x
                c = points[j].x*points[i].y-points[i].x*points[j].y
                points_dict[(a, b, c)] = points_dict.get((a, b, c), 0) + 1

            i += dup_count
        max_points = max(points_dict.values()) if points_dict else len(points)
        return max_points

p0 = Point(0, 0)
p1 = Point(1, -1)
p2 = Point(1, 1)
p3 = Point(1, 3)
p4 = Point(2, 3)
p5 = Point(-5, 3)
p6 = Point(3, 6)
p7 = Point(2, 4)

s = Solution()
print(s.maxPoints([p1, p2, p3]))
# print(s.maxPoints([p1, p2, p3, p4, p5, p6, p7]))