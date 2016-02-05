class Solution(object):
    def divide(self, dividend, divisor):
        """
        Implement division by minus, double the divisor if dividend is greater than divisor
        :param dividend: numerator
        :param divisor: denominator
        :return: quotient
        """
        quotient, quotient_temp = 0, 1
        dividend_temp, divisor_temp = abs(dividend), abs(divisor)
        sign = 1-2*((dividend < 0) != (divisor < 0))
        while abs(divisor) and dividend_temp >= abs(divisor):
            if dividend_temp >= divisor_temp:
                dividend_temp -= divisor_temp
                quotient += quotient_temp
                divisor_temp <<= 1
                quotient_temp <<= 1
            else:
                divisor_temp = abs(divisor)
                quotient_temp = 1

        return min(max(-(1 << 31), quotient*sign), (1 << 31)-1)


s = Solution()
print(s.divide(10, 1))


