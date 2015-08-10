__author__ = 'liangl2'
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        x1 = 1.0
        while True:
            x2 = 0.5*(x1+x/x1)
            if abs(x2-x1) <= 0.000000001:
                return x2
            x1 = x2
        return int(x2)


s = Solution()
print(s.mySqrt(0))