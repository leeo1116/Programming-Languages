class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """ ***************************************** O(n^2) **********************************************************
        if not nums:
            return 0
        nums_len = len(nums)
        max_len = [1]*nums_len
        for i in range(nums_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len[i] = max(max_len[i], max_len[j]+1)
        return max(max_len)
        *********************************************************************************************************** """

        temp = []
        for num in nums:
            pos = self.binary_search(temp, 0, len(temp), num)
            if pos > len(temp):
                temp.append(num)
            else:
                temp[pos] = num
        return len(temp)

    def binary_search(self, nums, start, stop, target):
        if start > stop:
            return -1
        mid = start+(stop-start)//2
        if nums[mid] < target:
            return self.binary_search(nums, mid+1, stop, target)
        elif nums[mid] > target:
            return self.binary_search(nums, start, mid-1, target)
        else:
            return mid


s = Solution()
nums1 = [1, 4, 6, 8, 9]
nums = [10, 9, 2, 5, 3, 4]
print(s.binary_search(nums1, 0, len(nums1)-1, 6))
print(s.lengthOfLIS(nums))