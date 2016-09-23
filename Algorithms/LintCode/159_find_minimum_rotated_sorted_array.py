class Solution(object):
    def find_min(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0] if nums else 0

    def find_min_binary_search(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left+(right-left)//2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid+1
        return nums[left]

s = Solution()
print(s.find_min_binary_search([1, 2, 3]))