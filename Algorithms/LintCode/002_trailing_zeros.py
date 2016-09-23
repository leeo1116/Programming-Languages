class Solution(object):
    def trailing_zeros(self, n):
        zeros_count = 0
        while n != 0:
            n //= 5
            zeros_count += n
        return zeros_count

s = Solution()
print(s.trailing_zeros(33))
