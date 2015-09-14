__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        i, j = 0, len(nums)-1
        four_sum_set = set()
        item_set = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            three_sum_set = threeSum(nums[i+1:], target-nums[i])
            four_sum_set =


        return list(item_set)

def threeSum(nums, target):
    if len(nums) < 3:
        return []
    item_set = set()
    for i in range(len(nums)-2):
        if i == 0 or nums[i] != nums[i-1]:
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == target:
                    item_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
    return list(item_set)

s = Solution()
# print(s.fourSum([5,5,3,5,1,-5,1,-2], 4))
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([-3,-1,0,2,4,5], 2))
# print(threeSum([-1, 0, 1], 0))


