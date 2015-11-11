import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        count = len(nums)-k
        while count:
            heapq.heappop(nums)
            count -= 1
        return heapq.heappop(nums)

    def find_kth_largest(self, nums, k):
        if k < 1 or k > len(nums):
            return None
        else:
            return self.find_kth_largest_helper(nums, 0, len(nums)-1, k)

    def find_kth_largest_helper(self, nums, start, end, k):
        left = start
        right = end
        pivot = left

        while left <= right:
            while left <= right and nums[left] <= nums[pivot]:
                left += 1
            while left <= right and nums[right] >= nums[pivot]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        if k == len(nums)-right:
            return nums[right]
        elif k < len(nums)-right:
            return self.find_kth_largest_helper(nums, right+1, end, k)
        else:
            return self.find_kth_largest_helper(nums, start, right-1, k)


s = Solution()
print(s.find_kth_largest([2, 1, 4, 5, 6], 3))
