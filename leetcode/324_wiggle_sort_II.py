class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        mid = (nums_len+1)//2
        j, k = nums_len-1, mid-1
        nums_sorted = sorted(nums)
        for i in range(nums_len):
            if i % 2:
                nums[i] = nums_sorted[j]
                j -= 1
            else:
                nums[i] = nums_sorted[k]
                k -= 1

    def wiggle_sort(self, nums):
        nums_len = len(nums)
        mid = nums_len // 2
        j = 0
        nums_sorted = sorted(nums)
        k = mid + 1 if nums_sorted[mid-1] == nums_sorted[mid] else mid
        for i in range(nums_len):
            if i % 2:
                nums[i] = nums_sorted[k]
                k += 1
            else:
                nums[i] = nums_sorted[j]
                j += 1

s = Solution()
nums1 = [1, 5, 1, 1, 6, 4]
nums2 = [1, 2, 3, 2, 1, 3]
nums3 = [1, 1, 2, 1, 2, 2, 1]
nums4 = [4, 5, 5, 6]
nums5 = [1, 3, 2, 2, 3, 1]
nums = nums5
s.wiggleSort(nums)
print(nums)
s.wiggle_sort(nums)
print(nums)
