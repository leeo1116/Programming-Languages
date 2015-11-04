__author__ = 'liangl2'
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return quotient
    # This method is very slow. Consider divisor increases by 2 times, divisor << 1


