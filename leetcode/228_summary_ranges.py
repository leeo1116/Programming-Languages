class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        m, n = nums[0], nums[0]
        ranges = []
        for i in range(1, len(nums)):
            if nums[i] == n+1:
                n = nums[i]
                if i == len(nums)-1:
                    if m < n:
                        ranges.append(str(m)+"->"+str(n))
                    if m == n:
                        ranges.append(str(m))
            else:
                if m < n:
                    ranges.append(str(m) + "->" + str(n))
                if m == n:
                    ranges.append(str(m))
                m = nums[i]
                n = nums[i]
                if i == len(nums) - 1:
                    ranges.append(str(m))
        return ranges


s = Solution()
print(s.summaryRanges([0, 1]))


