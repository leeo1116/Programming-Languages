__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if not nums:
            return False

        nums_sorted = [0]*len(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] < nums[i-1]:
                nums_sorted[:(len(nums)-i)] = nums[i:]
                nums_sorted[(len(nums)-i):] = nums[:i]
                break
            elif i == len(nums)-1:
                nums_sorted = nums

        low, high = 0, len(nums_sorted)-1
        while low <= high:
            mid = low+(high-low)//2
            if nums_sorted[mid] < target:
                low = mid+1
            elif nums_sorted[mid] > target:
                high = mid-1
            else:
                return True
        return False

s = Solution()
print(s.search([3, 1], 3))
