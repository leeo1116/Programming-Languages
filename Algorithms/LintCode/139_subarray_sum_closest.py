class Solution(object):
    def subarray_sum_closest(self, nums):
        prefix_sum_index, sum_tmp, interval = [(0, -1)], 0, [0, 0]
        for i in range(len(nums)):
            sum_tmp += nums[i]
            prefix_sum_index.append((sum_tmp, i))
        prefix_sum_index.sort()
        min_sum = prefix_sum_index[-1][0]-prefix_sum_index[0][0]
        for i in range(1, len(prefix_sum_index)):
            if prefix_sum_index[i][0]-prefix_sum_index[i-1][0] < min_sum:
                min_sum = prefix_sum_index[i][0]-prefix_sum_index[i-1][0]
                interval[0] = min(prefix_sum_index[i-1][1], prefix_sum_index[i][1])+1
                interval[1] = max(prefix_sum_index[i - 1][1], prefix_sum_index[i][1])
        return interval

s = Solution()
print(s.subarray_sum_closest([-3,1,1,-3,5]))

