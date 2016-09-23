class Solution(object):
    def sqrt(self, x):
        sqrt_x = 0
        while sqrt_x**2 <= x:
            sqrt_x += 1
        return sqrt_x-1

    def sqrt_binary_search(self, x):
        if x <= 1:
            return (x < 0) * -1 + (x == 1)
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1

s = Solution()
print(s.sqrt_binary_search(5))