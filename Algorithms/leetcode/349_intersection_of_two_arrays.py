class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect_num = []
        num1_freq = {}
        for num1 in nums1:
            num1_freq[num1] = 1

        for num2 in nums2:
            if num1_freq.get(num2, 0):
                intersect_num.append(num2)
                num1_freq[num2] -= 1

        return intersect_num


s = Solution()
print(s.intersection([1, 2, 2, 3, 4], [2, 4]))
