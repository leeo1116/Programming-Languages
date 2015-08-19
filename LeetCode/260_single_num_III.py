__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        num_dict = {}
        for num in nums:
            if num_dict.get(num, None):
                num_dict[num] += 1
                if num_dict[num] > 1:
                    del num_dict[num]
            else:
                num_dict[num] = 1
        return list(num_dict.keys())

s = Solution()
print(s.singleNumber([1, 2, 3, 3, 4, 5, 1, 2]))