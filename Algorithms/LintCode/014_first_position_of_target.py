class Solution(object):
    def binary_search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                return mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

s = Solution()
print(s.binary_search([2,6,8,13,15,17,17,18,19,20], 15))