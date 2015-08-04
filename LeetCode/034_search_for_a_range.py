__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        target_index = []
        index = self.binary_search(nums, target, 0, len(nums))
        while index != -1:
            target_index.append(index)
            nums[index] = nums[index]-0.1
            index = self.binary_search(nums, target, 0, len(nums))
        return target_index if target_index != [] else [-1, -1]

    def binary_search(self, nums, target, start, stop):
        if stop <= start:
            return -1
        m = (start+stop)//2
        if target > nums[m]:
            return self.binary_search(nums, target, m+1, stop)
        elif target < nums[m]:
            return self.binary_search(nums, target, start, m)
        else:
            return m


s = Solution()
print(s.searchRange([1], 1))