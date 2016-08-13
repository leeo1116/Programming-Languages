class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect_list = []
        # Traverse nums1 to calculate freq
        int_freq = dict()
        for num1 in nums1:
            if int_freq.get(num1, 0):
                int_freq[num1] += 1
            else:
                int_freq[num1] = 1
            # more elegant: int_freq[num1] = int_freq.get(num1, 0)+1

        # Traverse nums2 to find common integer
        for num2 in nums2:
            if int_freq.get(num2, 0):
                intersect_list.append(num2)
                int_freq[num2] -= 1

        return intersect_list


s = Solution()
print(s.intersect([1, 2, 4, 2], [2, 2, 2]))

# Follow up
# if both lists are sorted, using two cursors can solve this problem.
# if nums1[i] == nums2[j], intersect_list.append(nums1[i])
# elseif nums1[i] > nums2[j], j += 1
# else i += 1
