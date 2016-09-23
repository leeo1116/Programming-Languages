class Solution(object):
    def find_min(self, num):
        left, right = 0, len(num)-1
        while left < right:
            if num[left] < num[right]:
                return num[left]
            mid = left+(right-left)//2
            if num[mid] < num[left]:
                right = mid
            else:
                left = mid + 1
        return num[left]

s = Solution()
print(s.find_min([1, 1, 1, 3]))
