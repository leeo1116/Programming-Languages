__author__ = 'Liang Li'
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        for i, num in enumerate(nums):
            if nums_hash.get(target-num, None):
                return [nums_hash[target-num]+1, i+1]
            else:
                nums_hash[num] = i

s = Solution()
print(s.twoSum([3, 2, 4], 6))