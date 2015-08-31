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
        if len(points) < 2:
            return len(points)
        points_dict = {}
        for i in range(len(points)):
            dup_points = 0
            for j in range(i+1, len(points)):
                a = points[j].y-points[i].y
                b = points[i].x-points[j].x
                c = points[j].x*points[i].y-points[i].x*points[j].y
                abc_gcd = gcd(a, gcd(b, c))
                if abc_gcd:
                    a, b, c = a/abc_gcd, b/abc_gcd, c/abc_gcd
                else:
                    dup_points += 1
                points_dict[(a, b, c, i)] = points_dict.get((a, b, c, i), 0) + 1
            for key in points_dict:
                if key[-1] == i and key[:-1] != (0, 0, 0):
                    points_dict[key] += dup_points
        max_points = max(points_dict.values())+1
        return max_points

p0 = Point(0, 0)
p1 = Point(-1, -1)
p2 = Point(2, 2)
p3 = Point(2, 1)
p4 = Point(0, 1)
p5 = Point(0, 2)
p6 = Point(0, 3)

s = Solution()
print(s.maxPoints([p0, p0, p2, p2]))
