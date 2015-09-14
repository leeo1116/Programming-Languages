__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        # if num[i] is same to num[i - 1], then it needn't to be added to all of the subset,
        # just add it to the last l subsets which are created by adding S[i - 1]
        res = [[]]
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res)-l, len(res)):
                res.append(res[j]+[nums[i]])
        return res

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))