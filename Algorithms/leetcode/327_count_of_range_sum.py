class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums_len = len(nums)
        range_sum = [0]*(nums_len+1)  # why nums_len+1 instead of nums_len: to introduce S(0), so A(1) = S(1)-S(0)
        for i in range(nums_len):
            range_sum[i+1] = range_sum[i]+nums[i]
        return self.count_while_merge_sort(range_sum, 0, nums_len+1, lower, upper)  # why nums_len+1

    def count_while_merge_sort(self, sums, start, end, lower, upper):
        if end-start <= 1:  # why <= 1 instead of < 0 or <= 0
            return 0
        mid = start+(end-start)//2
        count = self.count_while_merge_sort(sums, start, mid, lower, upper)+self.count_while_merge_sort(sums, mid, end,
                                                                                                        lower, upper)
        i = j = k = mid
        range_sum_temp = [0]*(end-start)
        m = 0
        for n in range(start, mid):
            # Merge sort
            while k < end and sums[k] < sums[n]:  # right part[k] is smaller
                range_sum_temp[m] = sums[k]
                k += 1
                m += 1
            range_sum_temp[m] = sums[n]  # left part[n] is smaller
            m += 1

            while i < end and sums[i] - sums[n] < lower:
                i += 1
            while j < end and sums[j] - sums[n] <= upper:
                j += 1
            count += j - i

        sums[start:k] = range_sum_temp[:k-start]  # in-place assignment, merge sort complete
        return count

s = Solution()
print(s.countRangeSum([-2, 5, -1], -2, 2))



""" **********************************************Naive Solution O(n^2) ******************************************** """
        # nums_len = len(nums)
        # counter = 0
        # for i in range(nums_len):
        #     range_sum = 0
        #     for j in range(i, nums_len):
        #         range_sum += nums[j]
        #         if lower <= range_sum <= upper:
        #             counter += 1
        # return counter