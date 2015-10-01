__author__ = 'Liang Li'
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        return self.myPow(x*x, n/2) if n % 2 == 0 else self.myPow(x*x, n/2)*x
