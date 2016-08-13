__doc__ = """
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases. Notes: It is intended for this problem to be specified vaguely (ie, no given input
specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value. The string can contain additional characters after those
that form the integral number, which are ignored and have no effect on the behavior of this function.If the first
sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because
either str is empty or it contains only whitespace characters, no conversion is performed. If no valid conversion could
be performed, a zero value is returned. If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""

class Solution(object):
    def __init__(self, index):
        self.index = index

    def string_to_integer(self, s):
        """
        Convert string to integer, handle 4 cases
        1. all leading whitespaces
        2. sign of the number
        3. overflow
        4. invalid input
        :param s: input string
        :return integer: return integer
        """
        if not str:
            return 0
        i, sign, integer = 0, 1, 0
        max_int = (1 << 31)-1
        min_int = -(1 << 31)
        while s[i] == ' ':
            i += 1
        if s[i] in "+-":
            sign = 1-2*(s[i] == '-')
            i += 1
        while i < len(s) and '0' <= s[i] <= '9':
            if integer > max_int//10 \
                    or (integer == max_int//10 and ord(s[i])-ord('0') > max_int % 10):
                if sign == 1:
                    return max_int
                else:
                    return min_int
            integer = integer*10+ord(s[i])-ord('0')
            i += 1
        return integer*sign


s = Solution(8)
print(s.string_to_integer(' +13 12 '))
