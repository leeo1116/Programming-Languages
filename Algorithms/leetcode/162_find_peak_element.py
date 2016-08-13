class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_peak_element_helper(nums, 0, len(nums)-1)

    def find_peak_element_helper(self, nums, low, high):
        if low == high:
            return low
        else:
            mid1 = low+(high-low)//2
            mid2 = mid1+1
            if nums[mid1] > nums[mid2]:
                return self.find_peak_element_helper(nums, low, mid1)
            else:
                return self.find_peak_element_helper(nums, mid2, high)
