__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def median_of_two_sorted_array(self, nums1, nums2):
        if len(nums1) == 1 and nums1[0] > self.sorted_array_median(nums2):
            m, index = self.sorted_array_median(nums2)
            return self.sorted_array_median(nums2)
            return (nums1[0]+nums2[0])/2
        m1, index1 = self.sorted_array_median(nums1)
        m2, index2 = self.sorted_array_median(nums2)
        if m1 <= m2:
            nums1 = nums1[index1:]
            if len(nums2) > 1:
                nums2 = nums2[:index2]
            m = self.median_of_two_sorted_array(nums1, nums2)
        else:
            if len(nums1) > 1:
                nums1 = nums1[:index1]
            nums2 = nums2[index2:]
            m = self.median_of_two_sorted_array(nums1, nums2)
        return m

    def sorted_array_median(self, nums):
        array_len = len(nums)
        if array_len % 2 == 0:
            return (nums[array_len//2]+nums[array_len//2-1])/2, array_len//2
        return nums[array_len//2], array_len//2

s = Solution()
m = s.median_of_two_sorted_array([1, 2, 3, 8], [4, 5, 6, 7])
print(m)