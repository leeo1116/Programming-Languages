class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        # this is for python 2
        nums = map(str, nums)
        nums.sort(cmp=lambda a, b: cmp(a + b, b + a), reverse=True)
        return str(int(''.join(nums)))
