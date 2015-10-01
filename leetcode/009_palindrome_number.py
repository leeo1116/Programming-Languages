__author__ = 'liangl2'
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_reverse = reverse(x)
        if x_reverse == x:
            return True
        else:
            return False

def reverse(x):
    x_abs = abs(x)
    x_reverse = 0
    while x_abs:
        x_reverse, x_abs = x_reverse*10+x_abs%10, x_abs//10
    return x_reverse if x >= 0 else -x_reverse

x_rev = reverse(-234411)
print(x_rev)

s = Solution()
is_palindrome = s.isPalindrome(-23432)
print(is_palindrome)