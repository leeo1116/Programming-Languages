class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        result = []
        if numerator*denominator < 0:
            result.append('-')

        n = abs(numerator)
        d = abs(denominator)

        result.append(str(n//d))

        if n % d == 0:
            return ''.join(result)

        result.append('.')

        remainder_pos_dict = {}
        r = n % d
        while r:
            if remainder_pos_dict.get(r, None):
                result.insert(remainder_pos_dict[r], '(')
                result.append(')')
                break
            remainder_pos_dict[r] = len(result)
            r *= 10
            result.append(str(r//d))
            r %= d
        return ''.join(result)