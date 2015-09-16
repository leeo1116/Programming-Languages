__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        id = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[id] = nums[i]
                id += 1
        return id

s = Solution()
print(s.removeElement([3, 7], 0))