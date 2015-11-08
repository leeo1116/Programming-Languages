__author__ = 'Liang Li'
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        x_str = str(x)
        if x < 0:
            x_str = x_str[1:]
        x_str_reverse = ['']*len(x_str)
        for i in range(len(x_str)):
            x_str_reverse[len(x_str)-i-1] = x_str[i]
        x_reverse = int(''.join(x_str_reverse))
        if x_reverse < -2**(32-1)+1 or x_reverse > 2**(32-1)-1:
            return 0
        elif x < 0:
            return -x_reverse
        else:
            return x_reverse


class SolutionR:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
            x = -x
        r = 0
        while x:
            r = r*10+x%10
            x //= 10
        return r if x else -r


s = SolutionR()
print(s.reverse(-12))
integer_reverse = s.reverse(1)
print(integer_reverse)
