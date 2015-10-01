__author__ = 'Liang Li'
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 2:
            return n
        one_step, two_step = 2, 1
        while n-2:
            ways = one_step+two_step
            two_step = one_step
            one_step = ways

            n -= 1
        return ways

s = Solution()
print(s.climbStairs(4))