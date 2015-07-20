__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    item_sum = nums[i]+nums[j]+nums[k]
                    if abs(item_sum-target) < abs(closest_sum-target):
                        closest_sum = item_sum
                    if item_sum < target:
                        j += 1
                    else:
                        k -= 1
        return closest_sum

s = Solution()
print(s.threeSumClosest([0, 2, 1, -3], 1))