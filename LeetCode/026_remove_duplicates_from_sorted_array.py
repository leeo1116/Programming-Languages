__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        nums_len = len(nums)
        if nums_len < 2:
            return nums_len
        id = 1
        for i in range(1, nums_len):
            if nums[i] != nums[i-1]:
                nums[id] = nums[i]
                id += 1
        return id


s = Solution()
print(s.removeDuplicates([2, 3, 3, 4, 4, 5, 9]))