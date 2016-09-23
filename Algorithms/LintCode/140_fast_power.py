class Solution(object):
    def fast_power(self, a, b, n):
        if n == 1:
            return a%b
        if n == 0:
            return 1%b
        p = self.fast_power(a, b, n//2)
        p = (p*p)%b
        if n%2 == 1:
            p = (p*a)%b
        return p

s = Solution()
print(s.fast_power(3, 7, 5))
