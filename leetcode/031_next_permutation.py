__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        nums_len = len(nums)
        if nums_len <= 1:
            return
        for i in range(nums_len-1, 0, -1):
            if nums[i-1] < nums[i]:
                partition_num = nums[i-1]
                partition_index = i-1
                break
            if i == 1:
                partition_num = nums[0]
                partition_index = 0

        for i in range(nums_len-1, -1, -1):
            if nums[i] > partition_num:
                change_index = i
                break
            if i == partition_index:
                nums.reverse()
                return

        tmp = nums[change_index]
        nums[change_index] = nums[partition_index]
        nums[partition_index] = tmp
        if change_index == partition_index:
            nums.reverse()
        else:
            nums[:] = nums[:partition_index+1]+nums[:partition_index:-1]

class Solution_alt:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        nums_len = len(nums)
        if nums_len <= 1:
            return
        for i in range(nums_len-1, 0, -1):
            if nums[i-1] < nums[i]:
                partition_num = nums[i-1]
                partition_index = i-1
                break
            if i == 1:
                if nums[0] > nums[1]:
                    nums.reverse()
                    return
                partition_num = nums[0]
                partition_index = 0

        for i in range(nums_len-1, -1, -1):
            if nums[i] > partition_num:
                change_index = i
                break
            if i == partition_index:
                nums.reverse()
                return

        tmp = nums[change_index]
        nums[change_index] = nums[partition_index]
        nums[partition_index] = tmp
        nums[:] = nums[:partition_index+1]+nums[:partition_index:-1]

s = Solution()
a = [3, 2, 1]
s.nextPermutation(a)
print(a)
