__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1
        index = [-1, -1]
        # search for left index
        while low < high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid
        if nums[low] != target:
            return index
        else:
            index[0] = low

        # search for right index
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2+1
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid
        index[1] = high
        return index


s = Solution()
# print(s.searchRange([1, 1, 2, 4, 6, 8, 8, 10], 1))
print(s.searchRange([0, 1, 2, 3, 3, 4, 5, 6], 3))