__author__ = 'Liang Li'
# Solution1 utilize the two-sum function, time complexity is O(n^3)
class Solution1:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        index_list = []
        for i in range(len(nums)):
            sub_num = nums[i+1:]
            index1, index2 = two_sum(sub_num, 0-nums[i])
            while (index1, index2) != (-1, -1):
                sorted_num = [nums[i], sub_num[index1-1], sub_num[index2-1]]
                if sorted_num not in index_list:
                    index_list.append(sorted_num)
                sub_num[index1-1], sub_num[index2-1] = 0.1, 0.1
                index1, index2 = two_sum(sub_num, 0-nums[i])
        return index_list

def two_sum(nums, target):
    dict = {}
    index = 0
    for num in nums:
        if dict.get(target-num, None) is None:
            dict[num] = index
        else:
            return dict[target-num]+1, index+1
        index += 1
    return -1, -1

s = Solution1()
print(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        item_set = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                j = i+1
                k = len(nums)-1
                while j < k:
                    sum = nums[i]+nums[j]+nums[k]
                    if sum == 0:
                        item_set.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
        return list(item_set)

s = Solution()
print(s.threeSum([0, 0, 0]))
