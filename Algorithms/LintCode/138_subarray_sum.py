class Solution(object):
    def subarray_sum(self, nums):
        prefix_sum, prefix_sum_index = 0, {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum_index.get(prefix_sum, None) is not None:
                return [prefix_sum_index[prefix_sum]+1, i]
            prefix_sum_index[prefix_sum] = i
        return []

s = Solution()
print(s.subarray_sum([-3,1,2,-3,4]))
