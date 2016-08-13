class Solution(object):
    def search_insert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low < high:
            mid = low+(high-low)//2
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid
        return low if target <= nums[low] else low+1


s = Solution()
print(s.search_insert([1, 3], 4))